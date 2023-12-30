from fastapi import APIRouter, Request

import os
import json
import rblxopencloud

router = APIRouter()

privacy_states = {
    0: "SAFE_MODE",
    1: "PUBLIC",
    2: "PRIVATE",
    3: "WHITELIST",
    4: "TAKEN_DOWN"
}

experience = rblxopencloud.Experience(4398901283, api_key=os.environ['API_KEY'])
datastore = experience.get_data_store("Games", scope="global")

@router.get("/{worldId}", summary="Gets detailed world information by its ID.")
async def get_world(worldId: int):
  value = None
  info = None

  try:
    value, info = datastore.get(worldId)
  except:
    return {"error": "World not found"}

  data = {}
  data['name'] = value.get("Name")
  data['description'] = value.get("Description")
  data['placeId'] = value.get("GameId")
  data['visits'] = value.get("Visits")
  data['blocks'] = value.get("Blocks")
  data['allowedPrivateWorldUsers'] = value.get("PWhitelist")
  data['maxPlayers'] = value.get("MaxPlayers", 0)  # Set default value for maxPlayers
  data['activePlayers'] = value.get("ActivePlayers")
  data['whitelistedPlayers'] = value.get("Whitelisted", [])  # Set default empty list
  data['bannedPlayers'] = value.get("Banned")
  data['worldThumbnailId'] = value.get("Image")
  data['worldPrivacyState'] = privacy_states.get(value.get("State"), "UNKNOWN")
  data['serverId'] = value.get("Server")
  data['creator'] = value.get("Owner")

  return data