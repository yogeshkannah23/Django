from django.core.management.base import BaseCommand
from myblog.models import Post
from typing import Any

class Command(BaseCommand):

    help = "this will insert the post data"

    def handle(self,*args:Any,**options:Any):


        titles = [
            "The Forgotten Realm",
            "Echoes of Eternity",
            "Whispers in the Dark",
            "Stars Beyond Reach",
            "The Last Enchantment",
            "Shadow of the Eclipse",
            "Chronicles of the Celestial Wars",
            "City of Whispers",
            "The Alchemy of Fate",
            "Serpents of Silverlake",
            "Echoes from the Void",
            "Crown of Shadows",
            "Dreams of Glass",
            "Empire of Dust",
            "Blood Moon Rising",
            "The Crystal Key",
            "Sands of Time",
            "The Midnight Carnival",
            "Oracle of the Storms",
            "Beyond the Veil"
        ]

        descriptions = [
            "In a world where memories can be stolen, one woman must reclaim her past to save the future.",
            "A time-traveling historian discovers a hidden conspiracy that spans centuries.",
            "An investigative journalist uncovers a series of cryptic messages leading to a long-buried secret.",
            "Explorers on an interstellar mission encounter a sentient civilization on the brink of war.",
            "In a land where magic is fading, a reluctant hero must embark on a quest to restore its power.",
            "A detective hunts a serial killer who strikes only during solar eclipses, leaving ominous clues.",
            "Two rival factions of gods clash, forcing mortals to choose sides in an epic celestial war.",
            "In a dystopian future, a rebel group fights against a totalitarian regime using encrypted messages.",
            "A scientist discovers a formula that can alter destiny, leading to unforeseen consequences.",
            "A young sorcerer must unravel the mystery behind a lake that is cursed by ancient serpents.",
            "A spaceship crew investigates an abandoned colony only to find traces of an unknown alien race.",
            "A princess must navigate political intrigue and dark magic to claim her rightful throne.",
            "A journey through dreams and reflections, where reality blurs with the fragility of glass.",
            "In the ruins of an ancient empire, a new ruler rises amid whispers of rebellion and betrayal.",
            "Under a crimson sky, ancient prophecies foretell of a coming conflict that will reshape the world.",
            "Legend speaks of a key that unlocks the gateway to a realm of untold treasures and perilous secrets.",
            "Lost in the desert sands, a lone traveler discovers a forgotten city where time holds no sway.",
            "Beneath the carnival lights, mysteries unfold as darkness falls and the surreal becomes reality.",
            "A seer's visions ignite a quest across storm-tossed seas and into realms where gods and mortals collide.",
            "Beyond the veil lies a realm where shadows dance and ancient powers stir, awaiting a chosen champion."
        ]

        url_list = []
        for i in range(20):
            url_list.append(f"https://picsum.photos/id/{i}/800/400")
            # print(url_list)

        for title,content,img_url in zip(titles,descriptions,url_list):
            Post.objects.create(title=title,content=content,img_url=img_url)

        self.stdout.write(self.style.SUCCESS("Data inserted"))