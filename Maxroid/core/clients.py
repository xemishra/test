from pyrogram import Client
from pytgcalls import PyTgCalls

Maxroid = Client(
    "MaxroidMusic",
    api_id="28102624",
    api_hash="4e03913f9a576278ed4dbcdf7073e1b0",
    bot_token="7172527800:AAGazguW2jA-HawO8Wr9_ullifmXbEb0Zwc",
)

UserBot = Client(
    "xemishra",
    api_id="28102624",
    api_hash="4e03913f9a576278ed4dbcdf7073e1b0",
    session_string=str("BQGsz-AAFzuc0GghHHUbOtEUn727Jkz8uTaJuQP3LS5BHZxih4VuTdYM9_jbp2IEm3XLhNcsb1nzYtCAX9iVsGgeEWTgEfmxYyvm-zIZAzHSEgwmxWz4vv0_H19YhuMnt6N6f7W3mKt9Bu1_ccSrzIuko3tNdi4bVQXbcTfVUcNQyLGk4f0c8zCHmaujbPn1bToQaB305s2oegfPRHqdPnIBB98S2gxiABkjOHUg4mCC1cm8pvMmb8CrwrqPMwToyh-dZX7NgTEkQX5G7C2B2Fpfosy1dGB4j3NvD3Mq_5DcyHgXM0rlx7Xox5tEo_EhKhhMPLkq4bU96mkebXunxjeei4LxCwAAAAHTUBfqAA"),
)

xemishra = PyTgCalls(UserBot)
