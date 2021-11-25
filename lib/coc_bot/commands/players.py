import coc
from coc_bot.bot import bot, coc_client


@bot.command()
async def player_heroes(ctx, player_tag):
    print(vars(ctx))
    if not coc.utils.is_valid_tag(player_tag):
        await ctx.send("You didn't give me a proper tag!")
        return

    try:
        player = await coc_client.get_player(player_tag)
    except coc.NotFound:
        await ctx.send("This player doesn't exist!")
        return

    to_send = ""
    for hero in player.heroes:
        to_send += "{}: Lv{}/{}\n".format(str(hero), hero.level, hero.max_level)

    await ctx.send(to_send)
