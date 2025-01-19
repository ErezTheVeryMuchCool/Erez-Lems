import random
from datetime import datetime, timedelta

# Configuration: Number of robot tables and judging rooms
robot_tables = 2  # Example: 2 robot run tables
judging_rooms = 2  # Example: 2 judging rooms

# Teams data
teams = ['841', '3388', '941', '380', '1097', '123', '1695']

# Define constants
robot_run_time = timedelta(minutes=6)  # Duration of each robot run
robot_run_overlap_time = timedelta(minutes=3)  # Overlap of 3 minutes between robot runs
judging_session_time = timedelta(minutes=45)
buffer_time_range = (30, 60)  # buffer time between judging sessions (in minutes)

# Create the schedule
def create_schedule():
    start_time = datetime.strptime('10:00', '%H:%M')
    schedule = []

    # Robot runs with overlap and distribution across robot tables
    robot_runs = []
    table_count = 0  # Keep track of table usage
    for round in range(4):  # 4 robot runs per team
        for i in range(0, len(teams) - 1, robot_tables):  # Skip by the number of tables
            team_pair = teams[i:i + robot_tables]  # Create pairs of teams based on robot tables
            
            if len(team_pair) < 2:  # If there's not enough teams for this table, skip
                continue
            
            # Schedule robot run with overlap
            end_time = start_time + robot_run_time
            robot_runs.append({
                "Event": "Robot Run",
                "Teams": team_pair,
                "Start Time": start_time.strftime('%H:%M'),
                "End Time": end_time.strftime('%H:%M'),
                "Table": f"Table {table_count + 1}"  # Assign the robot run to a table
            })
            start_time = end_time - robot_run_overlap_time  # Allow overlap between runs
            
            table_count = (table_count + 1) % robot_tables  # Switch between tables

    # Judging sessions with room distribution
    start_time = datetime.strptime('17:00', '%H:%M')  # Start after robot runs
    team_batches = [teams[i:i + 4] for i in range(0, len(teams), 4)]  # 4 teams per judging session
    
    room_count = 0  # Keep track of room usage
    for batch in team_batches:
        start_time += timedelta(minutes=random.randint(*buffer_time_range))  # Random buffer time
        
        # Schedule judging session with room assignments
        round_end_time = start_time + judging_session_time
        schedule.append({
            "Event": "Judging Session",
            "Teams": batch,
            "Start Time": start_time.strftime('%H:%M'),
            "End Time": round_end_time.strftime('%H:%M'),
            "Room": f"Room {room_count + 1}"  # Assign the judging session to a room
        })
        start_time = round_end_time  # Update start time for the next judging session
        
        room_count = (room_count + 1) % judging_rooms  # Switch between judging rooms

    return robot_runs + schedule

# Display the schedule
schedule = create_schedule()
for entry in schedule:
    print(f"{entry['Event']} - Teams: {entry['Teams']} | Start: {entry['Start Time']} | End: {entry['End Time']} | {entry.get('Table', '')}{entry.get('Room', '')}")
