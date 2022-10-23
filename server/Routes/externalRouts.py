from fastapi import APIRouter, Response
from Routes import errorHandling
from Apis.myOutsourceApi import MyOutsourceApi

EXTERNAL_PLAYERS_API_BASE_URL = "https://recipes-goodness.herokuapp.com/"
router = APIRouter()


@router.get('/outsource/{ingredient}')
def get_players(response: Response, ingredient="cheese", gluten=False, dairy=False):
    response.headers['Access-Control-Allow-Origin'] = "*"
    caching_metadata = MyOutsourceApi(EXTERNAL_PLAYERS_API_BASE_URL).make_call("GET", f"recipes/{ingredient}").proccess_data(gluten, dairy)
    return caching_metadata

# note: later on add all CRUD operations