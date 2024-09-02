const { Client, Intents, REST, Routes } = require('discord.js');
const { token, clientId, guildId } = require('./config.json');
const ms = require('ms'); // Install ms package with npm install ms

const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

const commands = [
  {
    name: 'kick',
    description: 'Kick a user from the server',
    options: [
      { type: 'USER', name: 'target', description: 'User to kick', required: true },
      { type: 'STRING', name: 'reason', description: 'Reason for the kick', required: false },
    ],
  },
  {
    name: 'ban',
    description: 'Ban a user from the server',
    options: [
      { type: 'USER', name: 'target', description: 'User to ban', required: true },
      { type: 'STRING', name: 'reason', description: 'Reason for the ban', required: false },
    ],
  },
  {
    name: 'mute',
    description: 'Mute a user in the server',
    options: [
      { type: 'USER', name: 'target', description: 'User to mute', required: true },
      { type: 'STRING', name: 'duration', description: 'Duration to mute (e.g., 10m, 1h)', required: true },
    ],
  },
];

const rest = new REST({ version: '10' }).setToken(token);

(async () => {
  try {
    console.log('Started refreshing application (/) commands.');

    await rest.put(Routes.applicationGuildCommands(clientId, guildId), { body: commands });

    console.log('Successfully reloaded application (/) commands.');
  } catch (error) {
    console.error(error);
  }
})();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('interactionCreate', async interaction => {
  if (!interaction.isCommand()) return;

  const { commandName, options, member, guild } = interaction;

  if (commandName === 'kick') {
    const user = options.getUser('target');
    const reason = options.getString('reason') || 'No reason provided';

    if (!member.permissions.has('KICK_MEMBERS')) {
      return interaction.reply({ content: 'You do not have permission to kick members.', ephemeral: true });
    }

    const memberToKick = guild.members.cache.get(user.id);
    if (memberToKick) {
      try {
        await memberToKick.kick(reason);
        return interaction.reply(`${user.tag} has been kicked.`);
      } catch (error) {
        console.error(error);
        return interaction.reply({ content: 'There was an error while trying to kick the user.', ephemeral: true });
      }
    } else {
      return interaction.reply({ content: 'User not found.', ephemeral: true });
    }
  }

  if (commandName === 'ban') {
    const user = options.getUser('target');
    const reason = options.getString('reason') || 'No reason provided';

    if (!member.permissions.has('BAN_MEMBERS')) {
      return interaction.reply({ content: 'You do not have permission to ban members.', ephemeral: true });
    }

    const memberToBan = guild.members.cache.get(user.id);
    if (memberToBan) {
      try {
        await memberToBan.ban({ reason });
        return interaction.reply(`${user.tag} has been banned.`);
      } catch (error) {
        console.error(error);
        return interaction.reply({ content: 'There was an error while trying to ban the user.', ephemeral: true });
      }
    } else {
      return interaction.reply({ content: 'User not found.', ephemeral: true });
    }
  }

  if (commandName === 'mute') {
    const user = options.getUser('target');
    const duration = options.getString('duration');

    if (!member.permissions.has('MANAGE_ROLES')) {
      return interaction.reply({ content: 'You do not have permission to mute members.', ephemeral: true });
    }

    const memberToMute = guild.members.cache.get(user.id);
    if (memberToMute) {
      const role = guild.roles.cache.find(role => role.name === 'Muted');
      if (!role) {
        return interaction.reply({ content: 'Muted role does not exist. Please create a "Muted" role with no permissions.', ephemeral: true });
      }
      
      try {
        await memberToMute.roles.add(role);
        interaction.reply(`${user.tag} has been muted for ${duration}.`);

        setTimeout(async () => {
          await memberToMute.roles.remove(role);
          console.log(`${user.tag} has been unmuted.`);
        }, ms(duration));
      } catch (error) {
        console.error(error);
        return interaction.reply({ content: 'There was an error while trying to mute the user.', ephemeral: true });
      }
    } else {
      return interaction.reply({ content: 'User not found.', ephemeral: true });
    }
{
  "token": "YOUR_BOT_TOKEN_HERE",
  "clientId": "YOUR_CLIENT_ID_HERE",
  "guildId": "YOUR_GUILD_ID_HERE"
}

  }
});

client.login(token);
