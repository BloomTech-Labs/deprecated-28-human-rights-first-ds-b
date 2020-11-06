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
        "Example 4": "Officers issue calm, nonthreatening commands.",
        "Example 5": "The crowd was dispersed by police officers without incident.",
    },
    "Rank 2 - Empty-hand": {
        "Example 1": "Protesters are violently pushed onto the ground by officers.",
        "Example 2": "Protesters are being pushed and shoved by police.",
        "Example 3": "Police in riot gear charge peaceful crowd, beat them with shields.",
        "Example 4": "Officers use grabs, holds and joint locks to restrain an individual.",
        "Example 5": "Officers use punches and kicks to restrain an individual.",
    },
    "Rank 3 - Blunt Force": {
        "Example 1": "The police fire rubber bullets at the crowd.",
        "Example 2": "Police in riot gear fire bean bags at protesters.",
        "Example 3": "Police shooting riot rounds at protesters.",
        "Example 4": "Protesters are struck with batons by police officers.",
        "Example 5": "Blunt force impact. Officers may use a baton or projectile to immobilize.",
    },
    "Rank 4 - Chemical & Electric": {
        "Example 1": "Police use tear gas and pepper spray.",
        "Example 2": "Police in riot gear pepper spray protesters.",
        "Example 3": "Police deploy tear gas and flashbangs against protesters.",
        "Example 4": "Chemical. Officers may use chemical sprays or projectiles embedded with chemicals.",
        "Example 5": "Conducted Energy Devices. Officers use CEDs to immobilize an individual.",
    },
    "Rank 5 - Lethal Force": {
        "Example 1": "Protesters shot and killed by police.",
        "Example 2": "Police kill a protester.",
        "Example 3": "Police in riot gear open fire on a group of protesters.",
        "Example 4": "Police officers use deadly force.",
        "Example 5": "Police drive into a crowd killing several protesters.",
    },
}
