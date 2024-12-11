location_list = [
    "Port town",
    "Mountain pass",
    "Prairie",
    "Cross roads",
    "North meadow"
    "Capital city",
    "Hawk pass",
    "Elvenia",
    "Saven woods",
    "Toll bridge",
    "Hawk inn",
    "Bleak hills",
    "Old dungeon",
    "New dungeon",
    "Swamp",
    "Lake Gloria",
    "Dwarvenia"
]

connection_graph = {
    "Port Prospect": ["Mountain pass"],
    "Mountain pass": ["Port Prospect","Prairie"],
    "Prairie": ["Mountain pass","Cross roads"],
    "Cross roads": [
        "Prairie",
        "North meadow",
        "Toll bridge",
        "Old dungeon",
        "Swamp"
        ],
    "North meadow": ["Cross roads", "Capital city"],
    "Capital city": [
        "Hawk inn",
        "North meadow",
        "Lake Gloria"
        ],
    "Hawk inn": [
        "Capital city",
        "Hawk pass",
        "Bleak hills"
        ],
    "Hawk pass": ["Elvenia", "Hawk inn"],
    "Elvenia": ["Hawk pass", "Saven woods"],
    "Saven woods": ["Elvenia", "Toll bridge"],
    "Toll bridge": ["Saven woods", "Cross roads"],
    "Bleak hills": ["Hawk inn", "New dungeon"],
    "Old dungeon": ["Cross roads"],
    "New dungeon": ["Bleak hills"],
    "Swamp": ["Cross roads", "Dwarvenia" ],
    "Lake Gloria": ["Capital city", "Dwarvenia"],
    "Dwarvenia": ["Swamp", "Lake Gloria"]
}
