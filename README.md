# nueva-terra-bot

Discord bot for the [Nueva Terra](https://discord.gg/NqCFdtD8Xh) Minecraft Server.

## Running

Install [docker](https://www.docker.com/) with `docker-compose`.

```sh
cp .env.example .env
# Edit .env with your token, guild id and channel id.
docker-compose up
# Run with -d to run in the background.

# If ran with -d, use docker-compose logs to view logs, and docker-compose down to stop.
# If ran without -d, use Ctrl+C to stop.
```
