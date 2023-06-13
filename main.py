from fastapi import FastAPI
from router.router import router
from fastapi.middleware.cors import CORSMiddleware

main=FastAPI(title='CalidadAguaAPI')

origins = ["*"]
main.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


main.include_router(router)  



 
     
