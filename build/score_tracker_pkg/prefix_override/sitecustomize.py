import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fizzer/2026_competition_ws/install/score_tracker_pkg'
