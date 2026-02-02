import random

# -------------------------------------------------
# Data
# -------------------------------------------------

# Magical spellbook
spellbook: list[dict[str, str | bool]] = [
    {"name": "Wall of Light", "type": "Protection", "forbidden": False},
    {"name": "Infernal Flames", "type": "Destruction", "forbidden": True},
    {"name": "Frost Shield", "type": "Protection", "forbidden": False},
    {"name": "Arcane Nova", "type": "Destruction", "forbidden": False},
    {"name": "Shadow Portal", "type": "Summoning", "forbidden": True},
    {"name": "Healing Mist", "type": "Healing", "forbidden": False},
    {"name": "Lightning Spear", "type": "Destruction", "forbidden": False},
    {"name": "Purifying Aura", "type": "Protection", "forbidden": False},
    {"name": "Cursed Vortex", "type": "Destruction", "forbidden": True},
    {"name": "Ancient Spirit Invocation", "type": "Summoning", "forbidden": False},
    {"name": "Divine Restoration", "type": "Healing", "forbidden": False},
    {"name": "Mana Explosion", "type": "Destruction", "forbidden": False},
]

# Mission bank
missions: list[dict[str, str | list[str]]] = [
    {
        "description": "A magical storm threatens the forest. You must create a protective shield.",
        "required_spell_types": ["Protection"],
    },
    {
        "description": "Evil creatures are invading the region. You must destroy them.",
        "required_spell_types": ["Destruction"],
    },
    {
        "description": "An ancient spirit is enraged. You must summon an ally to calm it.",
        "required_spell_types": ["Summoning"],
    },
    {
        "description": "A nearby village has been struck by a magical disease. You must heal the wounded.",
        "required_spell_types": ["Healing"],
    },
    {
        "description": "A wall of fire blocks your path. You must protect yourself and destroy its source.",
        "required_spell_types": ["Protection", "Destruction"],
    },
    {
        "description": "A giant golem attacks! You must weaken it and protect yourself.",
        "required_spell_types": ["Destruction", "Protection"],
    },
    {
        "description": "An unstable portal threatens to swallow the region. You must summon a guardian and seal the portal.",
        "required_spell_types": ["Summoning", "Protection"],
    },
    {
        "description": "The undead are invading the forest. You must destroy them and purify the area.",
        "required_spell_types": ["Destruction", "Healing"],
    },
]

# -------------------------------------------------
# Helper functions
# -------------------------------------------------

def ask_include_forbidden_spells() -> bool:
    """Ask the user whether forbidden spells should be included."""
    while True:
        answer = input("Use forbidden spells? (Y/N): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Invalid input. Please enter Y or N.")


def filter_spells(
    spellbook: list[dict],
    required_types: list[str],
    include_forbidden: bool
) -> list[dict]:
    """
    Return spells that match the required types.
    Forbidden spells are included only if include_forbidden is True.
    """
    result = []
    for spell in spellbook:
        if spell["type"] in required_types:
            if include_forbidden or not spell["forbidden"]:
                result.append(spell)
    return result


def display_spells(spells: list[dict]) -> None:
    """Display the available spells with numbering."""
    for i, spell in enumerate(spells, start=1):
        label = " (Forbidden)" if spell["forbidden"] else ""
        print(f"{i}. {spell['name']}{label} — {spell['type']}")


def read_spell_choices(max_number: int) -> list[int]:
    """
    Read user input like '1,3' and return zero-based indices.
    """
    while True:
        raw = input("Choose spells [e.g.: 1,3]: ").strip()
        try:
            numbers = [int(x.strip()) for x in raw.split(",") if x.strip()]
        except ValueError:
            print("Invalid format. Example: 1,3")
            continue

        if not numbers:
            print("You must choose at least one spell.")
            continue

        if any(n < 1 or n > max_number for n in numbers):
            print(f"Please choose numbers between 1 and {max_number}.")
            continue

        # Remove duplicates while preserving order
        seen = set()
        indices = []
        for n in numbers:
            if n not in seen:
                indices.append(n - 1)
                seen.add(n)
        return indices


def check_required_spell_types(
    selected_spells: list[dict],
    required_types: list[str]
) -> tuple[bool, str]:
    """
    Check that:
    - enough spells are selected
    - each required spell type is present
    """
    if len(selected_spells) < len(required_types):
        return False, "Not enough spells selected."

    selected_types = {spell["type"] for spell in selected_spells}
    missing = [t for t in required_types if t not in selected_types]

    if missing:
        return False, f"Missing required spell type(s): {', '.join(missing)}."

    return True, ""


def apply_forbidden_spell_risk(selected_spells: list[dict]) -> tuple[bool, str]:
    """
    Each forbidden spell has a 50% chance to fail.
    If any forbidden spell fails, the mission fails immediately.
    """
    for spell in selected_spells:
        if spell["forbidden"]:
            if random.random() < 0.5:
                return False, f"BOOM 💥! The forbidden spell '{spell['name']}' exploded."
    return True, ""


# -------------------------------------------------
# Main game logic
# -------------------------------------------------

def play_mission(spellbook: list[dict], missions: list[dict]) -> None:
    """Run one random mission."""
    mission = random.choice(missions)

    print("\nYour mission:")
    print(mission["description"])

    required_types = mission["required_spell_types"]
    include_forbidden = ask_include_forbidden_spells()

    available_spells = filter_spells(
        spellbook, required_types, include_forbidden
    )

    if not available_spells:
        print("Mission failed ❌: No available spells for this mission.")
        return

    print("\nAvailable spells:")
    display_spells(available_spells)

    choices = read_spell_choices(len(available_spells))
    selected_spells = [available_spells[i] for i in choices]

    success, reason = check_required_spell_types(
        selected_spells, required_types
    )
    if not success:
        print("Mission failed ❌:", reason)
        return

    success, reason = apply_forbidden_spell_risk(selected_spells)
    if not success:
        print("Mission failed ❌:", reason)
        return

    print("\nMission successful! 🎉")
    print("You have overcome the challenge and earned the kingdom's admiration!")


if __name__ == "__main__":
    play_mission(spellbook, missions)
