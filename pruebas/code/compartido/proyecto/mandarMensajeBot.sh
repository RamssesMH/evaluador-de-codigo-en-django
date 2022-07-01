#!/usr/bin/env bash


api_token="1429640553:AAHkB0GoHWOWxXYkK0L4y0WctmGvaitPxQ8"
chat_id="849346770"
mensaje="$1"

function verMensajes() {
    curl https://api.telegram.org/bot${api_token}/getUpdates
}

curl -X POST \
     -H 'Content-Type: application/json' \
     -d "{\"chat_id\": \"849346770\", \"text\": \"${mensaje}\", \"disable_notification\": true}" \
     https://api.telegram.org/bot${api_token}/sendMessage
