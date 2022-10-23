from fastapi import APIRouter, Response
from Routes import errorHandling
from Database import dbQueries
from Apis.myOutsourceApi import MyOutsourceApi

EXTERNAL_PLAYERS_API_BASE_URL = "https://recipes-goodness.herokuapp.com/"
router = APIRouter()


@router.get('/outsource/{ingredient}')
def get_players(response: Response, ingredient="cheese", isDiary=False, isLectose=False):
    response.headers['Access-Control-Allow-Origin'] = "*"
    caching_metadata = MyOutsourceApi(EXTERNAL_PLAYERS_API_BASE_URL).make_call("GET", f"recipes/{ingredient}").proccess_data(isDiary, isLectose)
    return caching_metadata



# @router.post('/insource/')
# async def post(request: Request):
#     response = await request.json()   
#     key = list(response.keys())[0]     
#     val = response[key]
#     dbQueries.create_number(key, val)

#     print(response)
#     return response
