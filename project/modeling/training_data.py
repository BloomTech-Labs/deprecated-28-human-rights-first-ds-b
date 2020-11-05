"""
## The Use-of-Force Continuum - https://nij.ojp.gov/topics/articles/use-force-continuum

Rank I Officer Presence — No force is used. Considered the best way to resolve a situation.
The mere presence of a law enforcement officer works to deter crime or diffuse a situation.
Officers' attitudes are professional and nonthreatening.

Rank II Verbalization — Force is not-physical.
Officers issue calm, nonthreatening commands, such as "Let me see your identification and registration."
Officers may increase their volume and shorten commands in an attempt to gain compliance. Short commands might include "Stop," or "Don't move."

Rank III Empty-Hand Control — Officers use bodily force to gain control of a situation.
Soft technique. Officers use grabs, holds and joint locks to restrain an individual.
Hard technique. Officers use punches and kicks to restrain an individual.

Rank IV Less-Lethal Methods — Officers use less-lethal technologies to gain control of a situation.
Blunt impact. Officers may use a baton or projectile to immobilize a combative person.
Chemical. Officers may use chemical sprays or projectiles embedded with chemicals to restrain an individual (e.g., pepper spray).
Conducted Energy Devices (CEDs). Officers may use CEDs to immobilize an individual. CEDs discharge a high-voltage, low-amperage jolt of electricity at a distance.

Rank V Lethal Force — Officers use lethal weapons to gain control of a situation. Should only be used if a suspect poses a serious threat to the officer or another individual.
Officers use deadly weapons such as firearms to stop an individual's actions.
"""


ranked_reports = {
    "Rank 1 - Police Presence": {
        "Example 1": "Police in riot gear yell at protesters.",
        "Example 2": "Police blockade prevents marching to capitol steps.",
        "Example 3": "Police refused to answer when protesters asked why they were being arrested.",
        "Example 4": "Officers issue calm, nonthreatening commands, such as 'Let me see your identification and registration.'",
        "Example 5": "The crowd was dispersed by police officers without incident.",
    },
    "Rank 2 - Empty-hand Control": {
        "Example 1": "Protesters are quickly and violently pushed onto the ground, resulting in forceful removal.",
        "Example 2": "One individual can be seen bleeding from the mouth after being struck, before being pushed to the ground.",
        "Example 3": "Police in riot gear charge peaceful crowd, beat them with shields.",
        "Example 4": "Officers use grabs, holds and joint locks to restrain an individual.",
        "Example 5": "Officers use punches and kicks to restrain an individual.",
    },
    "Rank 3 - Blunt Force Trauma": {
        "Example 1": "The police fire rubber bullets at the crowd.",
        "Example 2": "Police in riot gear fire rubber bullets at protesters.",
        "Example 3": "Footage shows police shooting riot rounds at protesters in the zone.",
        "Example 4": "Protesters are struck with batons.",
        "Example 5": "Blunt force impact. Officers may use a baton or projectile to immobilize.",
    },
    "Rank 4 - Chemical & Electric Weapons": {
        "Example 1": "Police then retaliate against the crowd, firing tear gas and spraying pepper spray.",
        "Example 2": "Police in riot gear pepper spray protesters while marching.",
        "Example 3": "Police deploy tear gas and flashbangs against protesters.",
        "Example 4": "Chemical. Officers may use chemical sprays or projectiles embedded with chemicals.",
        "Example 5": "Conducted Energy Devices (CEDs). Officers use CEDs to immobilize an individual.",
    },
    "Rank 5 - Lethal Force": {
        "Example 1": "Protesters shot and killed by police.",
        "Example 2": "Police kill unarmed man for walking across the street.",
        "Example 3": "Police in riot gear open fire on a group of protesters for no reason.",
        "Example 4": "Officers use deadly force with weapons such as firearms.",
        "Example 5": "Police drive into a crowd killing several and injuring many more.",
    },
}
