import coc
import discord
from coc_bot.bot import bot, coc_client


@bot.command()
async def clan_info(ctx, clan_tag):
    if not coc.utils.is_valid_tag(clan_tag):
        await ctx.send("You didn't give me a proper tag!")
        return

    try:
        clan = await coc_client.get_clan(clan_tag)
    except coc.NotFound:
        await ctx.send("This clan doesn't exist!")
        return

    if clan.public_war_log is False:
        log = "Private"
    else:
        log = "Public"

    e = discord.Embed(colour=discord.Colour.green())
    e.set_thumbnail(url=clan.badge.url)
    e.add_field(
        name="Clan Name",
        value=f"{clan.name}({clan.tag})\n[Open in game]({clan.share_link})",
        inline=False,
    )
    e.add_field(name="Clan Level", value=clan.level, inline=False)
    e.add_field(name="Description", value=clan.description, inline=False)
    e.add_field(
        name="Leader", value=clan.get_member_by(role=coc.Role.leader), inline=False
    )
    e.add_field(name="Clan Type", value=clan.type, inline=False)
    e.add_field(name="Location", value=clan.location, inline=False)
    e.add_field(name="Total Clan Trophies", value=clan.points, inline=False)
    e.add_field(
        name="Total Clan Versus Trophies", value=clan.versus_points, inline=False
    )
    e.add_field(name="WarLog Type", value=log, inline=False)
    e.add_field(name="Required Trophies", value=clan.required_trophies, inline=False)
    e.add_field(name="War Win Streak", value=clan.war_win_streak, inline=False)
    e.add_field(name="War Frequency", value=clan.war_frequency, inline=False)
    e.add_field(name="Clan War League Rank", value=clan.war_league, inline=False)
    e.add_field(
        name="Clan Labels",
        value="\n".join(label.name for label in clan.labels),
        inline=False,
    )
    e.add_field(name="Member Count", value=f"{clan.member_count}/50", inline=False)
    e.add_field(
        name="Clan Record",
        value=f"Won - {clan.war_wins}\nLost - {clan.war_losses}\n Draw - {clan.war_ties}",
        inline=False,
    )
    await ctx.send(embed=e)


@bot.command()
async def clan_member(ctx, clan_tag):
    if not coc.utils.is_valid_tag(clan_tag):
        await ctx.send("You didn't give me a proper tag!")
        return

    try:
        clan = await coc_client.get_clan(clan_tag)
    except coc.NotFound:
        await ctx.send("This clan does not exist!")
        return

    member = ""
    for i, a in enumerate(clan.members, start=1):
        member += f"`{i}.` {a.name}\n"
    embed = discord.Embed(
        colour=discord.Colour.red(), title=f"Members of {clan.name}", description=member
    )
    embed.set_thumbnail(url=clan.badge.url)
    embed.set_footer(text=f"Total Members - {clan.member_count}/50")
    await ctx.send(embed=embed)


@bot.command()
async def current_war_status(ctx, clan_tag):
    if not coc.utils.is_valid_tag(clan_tag):
        await ctx.send("You didn't give me a proper tag!")
        return

    e = discord.Embed(colour=discord.Colour.blue())

    try:
        war = await coc_client.get_current_war(clan_tag)
    except coc.PrivateWarLog:
        return await ctx.send("Clan has a private war log!")

    if war is None:
        return await ctx.send("Clan is in a strange CWL state!")

    e.add_field(name="War State:", value=war.state, inline=False)

    if war.end_time:  # if state is notInWar we will get errors

        hours, remainder = divmod(int(war.end_time.seconds_until), 3600)
        minutes, seconds = divmod(remainder, 60)

        e.add_field(name=war.clan.name, value=war.clan.tag)
        e.add_field(
            name="Opponent:",
            value=f"{war.opponent.name}\n" f"{war.opponent.tag}",
            inline=False,
        )
        e.add_field(
            name="War End Time:",
            value=f"{hours} hours {minutes} minutes {seconds} seconds",
            inline=False,
        )

    await ctx.send(embed=e)
