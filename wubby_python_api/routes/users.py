from fastapi import APIRouter, Request

import os
import json
import rblxopencloud

router = APIRouter()

experience = rblxopencloud.Experience(4398901283, api_key=os.environ['API_KEY'])
datastore = experience.get_data_store("MyGames", scope="global")

@router.get("/{userId}", summary="Gets detailed user information by their ID.")
async def get_user(userId: int):
  value = None
  info = None
  
  try:
    value, info = datastore.get(userId)
  except:
    return {"error": "User not found"}
  
  data = {}
  data['description'] = value.get("Status")
  data['lastBanReason'] = value.get("Reason")
  data['wubbits'] = value.get("Wubbits")
  data['dailyLoginStreak'] = value.get("LR", [])[0]  # Handle potential missing LR list
  data['consecutiveLoginWubbits'] = value.get("LR", [])[1]
  data['joinDate'] = value.get("JoinDate")
  data['inventory'] = value.get("Inventory")
  data['equippedCosmetics'] = value.get("E", [])
  data['createdWorlds'] = value.get("Mine")
  data['favoriteWorlds'] = value.get("Favorites")
  data['recentWorlds'] = value.get("Recent")
  data['pinnedWorld'] = value.get("P")
  
  return data