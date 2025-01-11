from PyQt5.QtCore import QSettings
from rlbot.setup_manager import SetupManager, RocketLeagueLauncherPreference

from rlbot_gui.match_runner.match_runner import start_match_helper
from rlbot_gui.gui import get_bots_from_directory

human = {'name': 'Human', 'team': 0, 'type': 'human', 'skill': None, 'path': None}

def load_bots():
    BOT_FOLDER_SETTINGS_KEY = 'bot_folder_settings'

    def scan_for_bots(folder):
        return get_bots_from_directory(folder)

    def load_settings() -> QSettings:
        return QSettings('rlbotgui', 'preferences')

    settings = load_settings()
    global bot_folder_settings
    bot_folder_settings = settings.value(BOT_FOLDER_SETTINGS_KEY, type=dict)

    bot_list = []
    for folder_path in bot_folder_settings['folders'].keys():
        bot_list.extend(scan_for_bots(folder_path))
    
    return bot_list

bots = load_bots()

bots.append(human)
names = [bot['name'] for bot in bots]

print(names)
# pass

bot_list = []
bot_1 = bots[1]
bot_list.append({'name': bot_1['name'], 'team': 0, 'type': 'rlbot', 'skill': 1, 'path': bot_1['path']})
launcher_prefs = RocketLeagueLauncherPreference(preferred_launcher='steam', use_login_tricks=True, rocket_league_exe_path=None)

match_settings = {'map': 'DFHStadium', 'game_mode': 'Soccer', 'skip_replays': False, 'instant_start': False, 'enable_lockstep': False, 'match_behavior': 'Restart If Different', 'mutators': {'ball_bounciness': 'Default', 'ball_max_speed': 'Default', 'ball_size': 'Default', 'ball_type': 'Default', 'ball_weight': 'Default', 'boost_amount': 'Default', 'boost_strength': '1x', 'demolish': 'Default', 'game_speed': 'Default', 'gravity': 'Default', 'match_length': '5 Minutes', 'max_score': 'Unlimited', 'overtime': 'Unlimited', 'respawn_time': '3 Seconds', 'rumble': 'None', 'series_length': 'Unlimited'}, 'randomizeMap': False, 'enable_rendering': False, 'enable_state_setting': True, 'auto_save_replay': False, 'scripts': []}

start_match_helper(bot_list, match_settings, launcher_prefs)