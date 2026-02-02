import random

# -----------------------
# Data (given)
# -----------------------
grimoire: list[dict[str, str | bool]] = [
    {"nom": "Mur de Lumière", "type": "Protection", "interdit": False},
    {"nom": "Flammes Infernales", "type": "Destruction", "interdit": True},
    {"nom": "Bouclier de Givre", "type": "Protection", "interdit": False},
    {"nom": "Nova Arcanique", "type": "Destruction", "interdit": False},
    {"nom": "Portail de l'Ombre", "type": "Invocation", "interdit": True},
    {"nom": "Brume de Soins", "type": "Soin", "interdit": False},
    {"nom": "Lance de Foudre", "type": "Destruction", "interdit": False},
    {"nom": "Aura Purifiante", "type": "Protection", "interdit": False},
    {"nom": "Vortex Maudit", "type": "Destruction", "interdit": True},
    {"nom": "Invocation d'Esprit Ancien", "type": "Invocation", "interdit": False},
    {"nom": "Restauration Divine", "type": "Soin", "interdit": False},
    {"nom": "Explosion de Mana", "type": "Destruction", "interdit": False},
]

missions: list[dict[str, str | list[str]]] = [
    {"description": "Une tempête magique menace la forêt. Vous devez créer un bouclier protecteur.", "sorts_requis": ["Protection"]},
    {"description": "Des créatures maléfiques envahissent la région. Vous devez les éliminer.", "sorts_requis": ["Destruction"]},
    {"description": "Un esprit ancien est en colère. Vous devez invoquer un allié pour l'apaiser.", "sorts_requis": ["Invocation"]},
    {"description": "Un village voisin est frappé par une maladie magique. Vous devez soigner les blessés.", "sorts_requis": ["Soin"]},
    {"description": "Une barrière de feu bloque votre chemin. Vous devez créer un bouclier magique pour traverser.", "sorts_requis": ["Protection", "Destruction"]},
    {"description": "Un golem gigantesque attaque ! Vous devez l'affaiblir et vous protéger.", "sorts_requis": ["Destruction", "Protection"]},
    {"description": "Un portail instable menace d'engloutir la région. Vous devez invoquer une entité protectrice et sceller le portail.", "sorts_requis": ["Invocation", "Protection"]},
    {"description": "Les morts-vivants envahissent la forêt. Vous devez les éliminer et purifier la zone.", "sorts_requis": ["Destruction", "Soin"]},
]

# -----------------------
# Helper functions (English)
# -----------------------

def ask_include_forbidden() -> bool:
    while True:
        answer = input("Utilisez les sorts interdits ? (O/N) : ").strip().lower()
        if answer in ("o", "oui", "y", "yes"):
            return True
        if answer in ("n", "non", "no"):
            return False
        print("Réponse invalide. Tapez O ou N.")


def filter_spells(grimoire: list[dict], required_types: list[str], include_forbidden: bool) -> list[dict]:
    spells = []
    for spell in grimoire:
        if spell["type"] in required_types and (include_forbidden or not spell["interdit"]):
            spells.append(spell)
    return spells


def display_spells(spells: list[dict]) -> None:
    for i, spell in enumerate(spells, start=1):
        tag = " (Interdit)" if spell["interdit"] else ""
        print(f"{i}. {spell['nom']}{tag} — {spell['type']}")


def read_choices(max_choice: int) -> list[int]:
    while True:
        raw = input("Choisissez les sorts [ex. : 1,4] : ").strip()
        try:
            numbers = [int(x.strip()) for x in raw.split(",") if x.strip()]
        except ValueError:
            print("Format invalide. Exemple: 1,4")
            continue

        if not numbers:
            print("Vous devez choisir au moins un sort.")
            continue

        if any(n < 1 or n > max_choice for n in numbers):
            print(f"Choix hors limites. Entrez des nombres entre 1 et {max_choice}.")
            continue

        # remove duplicates
        seen = set()
        result = []
        for n in numbers:
            if n not in seen:
                result.append(n - 1)
                seen.add(n)
        return result


def check_required_types(selected_spells: list[dict], required_types: list[str]) -> tuple[bool, str]:
    if len(selected_spells) < len(required_types):
        return False, "Pas assez de sorts choisis."

    selected_types = {spell["type"] for spell in selected_spells}
    missing = [t for t in required_types if t not in selected_types]
    if missing:
        return False, f"Types manquants: {', '.join(missing)}."
    return True, ""


def apply_forbidden_risk(selected_spells: list[dict]) -> tuple[bool, str]:
    for spell in selected_spells:
        if spell["interdit"]:
            if random.random() < 0.5:
                return False, f"BOUM 💥 ! Le sort interdit '{spell['nom']}' a explosé."
    return True, ""


# -----------------------
# Main logic
# -----------------------

def play_mission(grimoire: list[dict], missions: list[dict]) -> None:
    mission = random.choice(missions)
    print("\nVotre mission :", mission["description"])

    required_types = mission["sorts_requis"]
    include_forbidden = ask_include_forbidden()

    available_spells = filter_spells(grimoire, required_types, include_forbidden)

    if not available_spells:
        print("Échec ❌ : Aucun sort disponible.")
        return

    print("\nSorts disponibles :")
    display_spells(available_spells)

    choices = read_choices(len(available_spells))
    selected_spells = [available_spells[i] for i in choices]

    ok, reason = check_required_types(selected_spells, required_types)
    if not ok:
        print("Échec ❌ :", reason)
        return

    ok, reason = apply_forbidden_risk(selected_spells)
    if not ok:
        print("Échec ❌ :", reason)
        return

    print("\nSuccès ✅ ! Mission accomplie ! 🤩")


if __name__ == "__main__":
    play_mission(grimoire, missions)
