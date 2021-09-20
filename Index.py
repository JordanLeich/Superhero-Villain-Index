import sys
import webbrowser
from modules import colors
from modules.Characters import *
import random

def create_characters():
    # Marvel Characters

    wolverine = Character('Wolverine', 'over 200', 'alive', 'Marvel', 'X-Men', 7, 4, 6, 3, 4, 5,
                          'superhuman strength and reflexes, enhanced senses and tracking abilities, and a special healing'
                          ' power that also slows his aging.',
                          125, 'images/portraits/wolverine.jpg')
    darwin = Character('Darwin', 'Unknown', 'alive', 'Marvel', 'X-Men', 5, 5, 5, 5, 5, 5,
                       'Superior Adaptation, Proactive Adaptation, Death Harbinger',
                       150, 'images/portraits/darwin.jpg')
    marvelgirl = Character('Marvel Girl', 'Unknown', 'alive', 'Marvel', 'X-Men', 4, 7, 4, 3, 6, 3,
                           'Telepathy, Empathy, Telekinesis, Time Manipulation',
                           125, 'images/portraits/marvel_girl.jpg')
    warpath = Character('Warpath', 'Unknown', 'alive', 'Marvel', 'Hellfire Club', 6, 1, 5, 3, 5, 5,
                        'Superhuman Physical Abilities, Flight, Regenerative Healing, Apache Shaman Abilities',
                        125, 'images/portraits/warpath.jpg')
    havok = Character('Havok', 'Unknown', 'alive', 'Marvel', 'X-Men', 3, 6, 3, 3, 2, 2,
                      'Ambient Energy Conversion, Energy Absorption, Plasma Emanation, Flight',
                      100, 'images/portraits/havok.jpg')
    multipleman = Character('Multiple Man', 'Unknown', 'alive', 'Marvel', 'X-Men', 4, 5, 3, 3, 4, 3,
                            'Kinetic Duplication, Duplication Experience Transference, Duplication Healing',
                            100, 'images/portraits/multiple_man.jpg')
    colossus = Character('Colossus', 'Unknown', 'alive', 'Marvel', 'X-Men', 6, 0, 4, 3, 3, 7,
                         'Enhanced Mutant Physiology, Organic Steel Form, Superhuman Strength',
                         75, 'images/portraits/colossus.jpg')
    blob = Character('Blob', 'Unknown', 'alive', 'Marvel', 'Brotherhood of Mutants', 6, 2, 3, 2, 2, 4,
                     'Superhuman Durability and Strength, Pain Immunity, Trapping, Projectile Redirection, Mass Shifting',
                     50, 'images/portraits/blob.png')
    sabretooth = Character('Sabretooth', 'Unknown', 'alive', 'Marvel', 'X-Men', 4, 1, 7, 2, 2, 4,
                           'Regenerative Healing Factor, Superhuman Senses, Adamantium Claws, Fangs',
                           60, 'images/portraits/sabretooth.jpg')
    cyclops = Character('Cyclops', 'Unknown', 'alive', 'Marvel', 'X-Men', 3, 7, 3, 5, 4, 4,
                        'Optic Blast, Trajectory Bending, Spatial Awareness, Energy Resistance',
                        45, 'images/portraits/cyclops.jpg')
    silversamurai = Character('Silver Samurai', 'Unknown', 'alive', 'Marvel', 'Big Hero 6', 4, 5, 6, 3, 2, 3,
                              'Tachyon Field, Kenjutsu, Bushido, Martial Arts',
                              65, 'images/portraits/silver_samurai.jpg')
    mystique = Character('Mystique', 'Unknown', 'alive', 'Marvel', 'Brotherhood of Mutants', 4, 0, 5, 4, 2, 2,
                         'Metamorph, Psychic Defense, Accelerated Healing, Toxin and Disease Resistance, Metamorphic Adaptation',
                         40, 'images/portraits/mystique.jpg')
    banshee = Character('Banshee', 'Unknown', 'alive', 'Marvel', 'X-Men', 3, 7, 4, 3, 4, 2,
                        'Acoustikinesis, Sonic Scream, Flight, Sonar, Sonic Shield, Vocal Disorientation, Vocal Trance, Sound Immunity, Superhuman Vocal Stamina',
                        75, 'images/portraits/banshee.jpg')
    magneto = Character('Magneto', 'Unknown', 'alive', 'Marvel', 'Brotherhood of Mutants', 2, 6, 4, 5, 5, 2,
                        'Magnetokinesis, Magnetic Force-Fields, Magnetic Armor, Flight, Metal Manipulation, Organic Iron Manipulation, Electromagnetic Spectrum Manipulation',
                        40, 'images/portraits/magneto.jpg')
    professorx = Character('Professor X', 'Unknown', 'alive', 'Marvel', 'X-Men', 0, 3, 1, 7, 0, 0,
                           'Telepathy, Telepathic Illusions, Telekinesis, Astral Projection, Mental Shield, Psionic Blasts, Mental Detection, Mind Possession, Mind Control',
                           25, 'images/portraits/professor_x.jpg')
    callisto = Character('Callisto', 'Unknown', 'alive', 'Marvel', 'Morlocks', 4, 2, 7, 4, 5, 4,
                         'Superhuman Senses, Regenerative Healing, Intuitive Tactical Ability',
                         35, 'images/portraits/callisto.jpg')
    laurakinney = Character('X-23', 'Unknown', 'alive', 'Marvel', 'X-Men', 7, 3, 7, 5, 7, 7,
                            'Regenerative Healing Factor, Bone Claws, Psychic Defenses, Chemical Immunity, Disease Immunity, Superhuman Senses',
                            80, 'images/portraits/laura_kinney.jpg')
    iceman = Character('Iceman', 'Unknown', 'alive', 'Marvel', 'X-Men', 4, 5, 3, 2, 4, 3,
                       'Thermokinesis, Cryokinesis, Organic Ice-Form, Hydrokinesis, Cellular Replacement',
                       45, 'images/portraits/iceman.jpg')
    blink = Character('Blink', 'Unknown', 'alive', 'Marvel', 'X-Men', 2, 4, 4, 3, 7, 2,
                      'Teleportation Warp Portals, Trans-Spatial Displacement Bills',
                      60, 'images/portraits/blink.jpg')
    omegared = Character('Omega Red', 'Unknown', 'alive', 'Marvel', 'Red Mafia', 5, 4, 6, 4, 3, 5,
                         'Death Factor, Life Force Absorption, Superhuman Strength, Regenerative Healing Factor',
                         80, 'images/portraits/omega_red.jpg')
    mistersinister = Character('Mister Sinister', 'Unknown', 'alive', 'Marvel', 'Roxxon', 6, 6, 6, 7, 5, 5,
                               'Genetic Enhancements Using Mutant DNA, Endopathy, Cellular Shape-Shifting, Regenerative Healing Factor, Superhuman Physical Condition, Telepathy'
                               'Telekinesis, Technology Interface, Teleportation', 95,
                               'images/portraits/mister_sinister.jpg')
    shadowking = Character('Shaodw King', 'Unknown', 'alive', 'Marvel', 'Brotherhood of Mutants', 7, 5, 1, 3, 7, 1,
                           'Telepathy, Astral Form, Anchor Host',
                           100, 'images/portraits/shadow_king.jpg')
    beast = Character('Beast', 'Unknown', 'alive', 'Marvel', 'X-Men', 4, 1, 4, 6, 3, 4,
                      'Genetic Atavism, Superhuman Physical Traits, Regenerative Healing Factor, Superhuman Senses, Razor-Sharp Claws and Fangs',
                      60, 'images/portraits/beast.jpg')
    daken = Character('Daken', 'Unknown', 'alive', 'Marvel', 'X-Factor', 4, 0, 7, 2, 3, 4,
                      'Mutant Physiology, Regenerative Healing Factor, Disease Immunity, Superhuman Physical Traits, Retractable Bone Claws, Anti-Healing Factor Claws',
                      70, 'images/portraits/daken.jpg')
    deathbird = Character('Deathbird', 'Unknown', 'alive', 'Marvel', 'The Brood Horsemen of Apocalypse Starforce', 3, 1,
                          6, 3, 2, 4, 'Claws, Natural Winged Flight',
                          75, 'images/portraits/deathbird.jpg')
    emmafrost = Character('Emma Frost', 'Unknown', 'alive', 'Marvel', 'Brotherhood of Mutants', 7, 7, 6, 7, 4, 5,
                          'Telepathy, Psionic Shield, Astral Projection, Mind Control, Mental Alteration, Psionic Blasts',
                          125, 'images/portraits/emma_frost.jpg')
    blackheart = Character('Blackheart', 'Unknown', 'alive', 'Marvel', 'Hellfire Club', 7, 6, 5, 6, 6, 6,
                           'Superhuman Physical Traits, Telepathy, Levitation, Interdimensional Teleportation, Size Alteration, Physical Alteration, Regenerative Healing,'
                           'Energy Generation, Soul Capturing, Mind Control', 150, 'images/portraits/blackheart.jpg')
    angel = Character('Angel', 'Unknown', 'alive', 'Marvel', 'X-Men', 4, 1, 3, 3, 3, 3,
                      'Wings, Flight, Aerial Adaptation, Regenerative Healing Factor, Hypersonic Scream',
                      50, 'images/portraits/angel.jpg')
    gladiator = Character('Gladiator', 'Unknown', 'alive', 'Marvel', 'Imperial Guard', 6, 6, 6, 4, 6, 7,
                          'Superhuman Physical Traits, Flight, Heat Beams, Microscopic Vision, Super Breath, Psionic Resistance, Accelerated Healing Factor',
                          100, 'images/portraits/gladiator.jpg')
    mimic = Character('Mimic', 'Unknown', 'alive', 'Marvel', 'X-Men', 4, 6, 4, 4, 5, 5, 'Power Mimicry',
                      150, 'images/portraits/mimic.jpg')
    apocalypse = Character('Apocalypse', 'unknown', 'alive', 'Marvel', 'Four Horsemen', 6, 7, 7, 7, 7, 7,
                           'Immortality, Superhuman Physical Traits, Teleportation, Psionic Manipulation, Telekinesis, Flight, Telepathy, Self-Molecular Manipulation'
                           'Celestial Energy Manipulation',
                           200, 'images/portraits/apocalypse.jpg')
    deadpool = Character('Deadpool', 'Unknown', 'alive', 'Marvel', 'X-Force', 5, 1, 6, 4, 7, 5,
                         'Genetically Enhanced Physiology, Healing Factor, Immortality, Telepathic Immunity, Disease Immunity',
                         150, 'images/portraits/deadpool.jpg')
    storm = Character('Storm', 'Unknown', 'alive', 'Marvel', 'X-Men', 5, 6, 5, 5, 6, 4,
                      'Atmokinesis, Telepathic Resistance, Earth Link, Thermal Variance, Energy Vision, Magical Potential',
                      85, 'images/portraits/storm.jpg')
    mrfantastic = Character('Mr. Fantastic', 'Unknown', 'alive', 'Marvel', 'Fantastic Four', 6, 1, 3, 6, 2, 3,
                            'Plasticity, Elongation, Shape Changing, Superhuman Intellect',
                            75, 'images/portraits/mister_fantastic.jpg')
    invisiblewoman = Character('Invisible Woman', 'Unknown', 'alive', 'Marvel', 'Fantastic Four', 5, 7, 4, 5, 3, 3,
                               'Invisibility, Psionic Force Fields, Cosmic Ray Blasts',
                               75, 'images/portraits/invisible_woman.jpg')
    thething = Character('The Thing', 'Unknown', 'alive', 'Marvel', 'Fantastic Four', 6, 1, 4, 2, 2, 6,
                         'Rock-like Sin, Superhuman Strength, De-Aging Abilities, Sensory Adaptation',
                         60, 'images/portraits/the_thing.jpg')
    humantorch = Character('Human Torch', 'Unknown', 'alive', 'Marvel', 'Fantastic Four', 3, 6, 4, 4, 5, 3,
                           'Pyrogenesis, Plasma Form, Pyrokinesis, Nova Flame, Flight, Thermokinesis',
                           60, 'images/portraits/human_torch.jpg')
    doctordoom = Character('Doctor Doom', 'Unknown', 'alive', 'Marvel', 'Legion of Doom', 6, 6, 4, 6, 5, 4,
                           'Magic, Mystical Blasts, Psionics, Super-Genius Intelligence, Mind Transference, Healing, Dimensional Travel, Spell Casting',
                           75, 'images/portraits/doctor_doom.jpg')
    forge = Character('Forge', 'Unknown', 'alive', 'Marvel', 'X-Men', 2, 1, 4, 4, 2, 2, 'Intuitive Genius, Sorcery',
                      55, 'images/portraits/forge.jpg')
    bishop = Character('Bishop', 'Unknown', 'alive', 'Marvel', 'X-Men', 4, 7, 5, 4, 2, 3,
                       'Energy Absorption, Accelerated Healing, Energy Conversion, Concussive Blasts, Energy Resistance, Superhuman Physical Traits',
                       70, 'images/portraits/bishop.jpg')
    psylocke = Character('Psylocke', 'Unknown', 'alive', 'Marvel', 'X-Men', 3, 6, 6, 4, 3, 3,
                         'Telepathy, Psionic Knife, Psionic Blasts, Astral Projection, Telekinesis, Reality Anchoring, Flight, Force Fields, Precognition, Psionic Shadow',
                         60, 'images/portraits/psylocke.jpg')
    sunspot = Character('Sunspot', 'Unknown', 'alive', 'Marvel', 'X-Men', 4, 7, 5, 4, 4, 5,
                        'Solar Radiation Absorption, Solar Re-channeling, Flight, Enhanced Strength, Thermokinesis, Dark Solar Blasts, Energy Absorption',
                        65, 'images/portraits/sunspot.png')
    sage = Character('Sage', 'Unknown', 'alive', 'Marvel', 'X-Men', 2, 0, 5, 6, 4, 3,
                     'Mental Computation, Photographic Memory, Kinetic Memory, Biokinesis, Self Mastery, Telepathy',
                     60, 'images/portraits/sage.jpg')
    domino = Character('Domino', 'Unknown', 'alive', 'Marvel', 'X-Force', 3, 3, 6, 3, 3, 2,
                       'Power Manipulation, Enhanced Agility and Reflexes, Luck, Probability Manipulation',
                       60, 'images/portraits/domino.jpg')
    rogue = Character('Rogue', 'Unknown', 'alive', 'Marvel', 'X-Men', 6, 6, 6, 6, 6, 6,
                      'Power Absorption, Power Enhancements, Ionic Energy Form, Flight, Immortality',
                      125, 'images/portraits/rogue.jpg')
    gambit = Character('Gambit', 'Unknown', 'alive', 'Marvel', 'X-Men', 3, 5, 4, 3, 3, 3,
                       'Molecular Acceleration, Accelerated Regeneration, Hypnotic Charm, Mutant Energy Control',
                       60, 'images/portraits/gambit.jpg')
    captainbritain = Character('Captain Britain', 'Unknown', 'alive', 'Marvel', 'Secret Avengers', 6, 3, 4, 5, 4, 6,
                               'Interdimensional Energy Blasts, Superhuman Strength, Flight, Genius Intelligence',
                               90, 'images/portraits/captain_britain.jpg')
    jubilee = Character('Jubilee', 'Unknown', 'alive', 'Marvel', 'X-Men', 5, 7, 5, 4, 4, 4,
                        'Explosive Light Blasts, Energy Plasmoids, Psionic Shields',
                        90, 'images/portraits/jubilee.jpg')
    kittypryde = Character('Kitty Pryde', 'Unknown', 'alive', 'Marvel', 'X-Men', 3, 2, 4, 4, 2, 2,
                           'Phasing, Intagibility, Telepathic Resistance, Black Vortex',
                           65, 'images/portraits/kitty_pryde.jpg')
    nightcrawler = Character('Nightcrawler', 'Unknown', 'alive', 'Marvel', 'X-Men', 5, 5, 5, 4, 7, 4,
                             'Teleportation, Acrobatics, Spatial Awareness, Tail Grab',
                             85, 'images/portraits/nightcrawler.jpg')
    cable = Character('Cable', 'Unknown', 'alive', 'Marvel', 'X-Force', 4, 4, 6, 3, 6, 4,
                      'Telepathy, Psionic Shield, Psionic Blasts, Telekinesis, Force Fields, Time Travel, Techno-Organic Physiology',
                      100, 'images/portraits/cable.jpg')
    juggernaut = Character('Juggernaut', 'Unknown', 'alive', 'Marvel', 'Brotherhood of Mutants', 7, 1, 3, 2, 4, 7,
                           'Demonic Empowerment, Superhuman Strength',
                           125, 'images/portraits/juggernaut.jpg')
    daredevil = Character('Daredevil', 'Unknown', 'alive', 'Marvel', 'Defenders', 2, 4, 5, 3, 2, 3,
                          'Superhuman Sensory, Superhuman Reflexes, Blindsight, Radar Sense, Acrobats, Martial Arts',
                          60, 'images/portraits/daredevil.jpg')
    doctorstrange = Character('Doctor Strange', 'Unknown', 'alive', 'Marvel', 'Avengers', 3, 7, 3, 5, 6, 3,
                              'Sorcery, Energy Blasts, Astral Projection, Transmutation, Telekinesis, Telepathy, Flight, Protective Shields, Universal Awareness',
                              100, 'images/portraits/drstrange.jpg')
    hawkeye = Character('Hawkeye', 'Unknown', 'alive', 'Marvel', 'Avengers', 3, 1, 5, 3, 3, 3,
                        'Master Archery, Superhuman Sight, Master Marksmanship, Master Martial Arts, Weapon Proficiency',
                        60, 'images/portraits/hawkeye.jpg')
    hulk = Character('Hulk', 'Unknown', 'alive', 'Marvel', 'Avengers', 7, 5, 4, 6, 3, 7,
                     'Transformation, Unlimited Strength, Self-Regeneration, Super-Genius Intelligence',
                     100, 'images/portraits/hulk.jpg')
    spiderman = Character('Spider-Man', 'Unknown', 'alive', 'Marvel', 'Avengers', 3, 1, 4, 5, 4, 5,
                          'Wall Crawling, Superhuman Strength, Regenerative Healing Factor, Spider-Sense, Indomitable Will, Gifted Intellect, Expert Engineer, Acrobats',
                          90, 'images/portraits/spiderman.jpg')
    thor = Character('Thor', 'Unknown', 'alive', 'Marvel', 'Avengers', 6, 6, 4, 2, 6, 7,
                     'Superhuman Physical Traits, Flight, Allspeak, Odin Force, Energy Blasts, Lightning Blasts, Weather Manipulation, Mjolnir Strikes',
                     150, 'images/portraits/thor.jpg')
    captainamerica = Character('Captain America', 'Unknown', 'alive', 'Marvel', 'Avengers', 4, 1, 6, 3, 3, 4,
                               'Super-Soldier Strength, Master Tactician, Master Strategist, Master Martial Arts, Indomitable Will, Weapon Proficiency',
                               100, 'images/portraits/captainamerica.jpg')
    loki = Character('Loki', 'Unknown', 'alive', 'Marvel', 'No Affiliations', 5, 6, 3, 5, 7, 5,
                     'Regenerative Healing Factor, Sorcery, Shapeshifting, Transmutation, Enchantments',
                     115, 'images/portraits/loki.jpg')
    thanos = Character('Thanos', 'Unknown', 'alive', 'Marvel', 'No Affiliation', 7, 7, 6, 6, 7, 7,
                       'Godlike Strength, Near-Invulnerability, Regenerative Healing Factor, Energy Manipulation, Telepathy, Magic, Teleportation',
                       200, 'images/portraits/thanos.jpg')
    ironman = Character('Ironman', 49, 'alive', 'Marvel', 'Avengers', 6, 6, 4, 6, 5, 6, 'Super-Genius Intelligence, Energy Blasts, Thruster Attacks, Pulse Blasts, Repulsor Shot',
                        150, 'images/portraits/ironman.jpg')

    # DC Characters

    batman = Character('Batman', 'Unknown', 'alive', 'DC', 'Justice League', 4, 3, 7, 7, 2, 5,
                       'Acrobatics, Athletics, gadgetry, Intimidation, Martial Arts, Stealth, Tactical Analysis',
                       100, 'images/portraits/batman.jpg')
    superman = Character('Superman', 'Unknown', 'alive', 'DC', 'Justice League', 7, 6, 4, 4, 7, 7,
                         'Solar Energy Absorption, Cosmic Energy Absorption, Unlimited Strength, Flight, Heat Vision, Super-Breath',
                         175, 'images/portraits/superman.jpg')
    joker = Character('Joker', 'Unknown', 'alive', 'DC', 'No Affiliation', 3, 3, 6, 6, 2, 2,
                      'Pain Resistance, Tainted Blood, Cheating Death, Trickery',
                      90, 'images/portraits/joker.jpg')

    # Mortal Kombat Characters

    ermac = Character('Ermac', 'Unknown', 'alive', 'Mortal Kombat', 'No Affiliation', 3, 5, 6, 4, 3, 3,
                      'Teleport Punch, Telekinetic Slam, Hado-Energy, Soul Ball, Soul Burst, Mystic Bomb, Telekinetic Throw, Force Push',
                      80, 'images/portraits/ermac.png')
    scorpion = Character('Scorpion', 'Unknown', 'alive', 'Mortal Kombat', 'No Affiliation', 4, 4, 6, 3, 3, 3,
                         'hellfire Punch, Leg Takedown, Air Throw, Fire Breath, Demon Fire, Fire Ball, Death Spin, Burning Spear',
                         80, 'images/portraits/scorpion.jpg')
    shaokahn = Character('Shao Kahn', 'Unknown', 'alive', 'Mortal Kombat', 'No Affiliation', 6, 6, 7, 7, 3, 6,
                         'Charging Spikes, Wrath Hammer, Explosive Ball, Emperor\'s Shield, Mystic Choke, Hammer Throw, Ground Shatter',
                         150, 'images/portraits/shaokahn.jpg')

    return [wolverine, darwin, marvelgirl, warpath, havok, multipleman, colossus, blob, sabretooth, cyclops,
            silversamurai, mystique, banshee, magneto, professorx, callisto, laurakinney, iceman, blink, omegared,
            mistersinister, shadowking,
            beast, daken, deathbird, emmafrost, blackheart, angel, gladiator, mimic, apocalypse, deadpool, storm,
            mrfantastic, invisiblewoman, thething, humantorch, doctordoom, forge, bishop, psylocke, sunspot, sage,
            domino, rogue, gambit,
            captainbritain, jubilee, kittypryde, nightcrawler, cable, juggernaut, daredevil, doctorstrange, hawkeye,
            hulk, spiderman, thor, captainamerica, loki, thanos, ironman, batman, superman, joker, ermac, scorpion, shaokahn]


characters = create_characters()

def findcharacter(character):

    for c in characters:
        if character.lower() == c.name.lower():
            time.sleep(2)
            return c

    if character.lower() != c.name.lower():
        print(colors.red + 'Superhero/Villain name not found!', colors.reset, '\n')
        write_to_text_choice = str(input(
            'Would you like to add this superhero/villain name to a text file so that the developers know who to add '
            '(yes / no): '))
        print()
        if write_to_text_choice.lower() in ['y', 'yes', 'sure']:
            request_a_character(character)
        elif write_to_text_choice.lower() in ['n', 'no', 'nope']:
            start()
        else:
            error_message()

def charactertotal(character):  # Gets total value from all of the characters traits
    return character.durability + character.energy + character.fighting + character.intelligence + character.speed + character.strength

def onevone(first_character, second_character):
    if first_character.fighting > second_character.fighting:    # Checks which fighter has a higher fighting stat to get a slight bonus
        char1_total = charactertotal(first_character) + random.randint(0, 6) + random.randint(0, 6)  # bonuses are distributed randomly in order to give the character with less fighting stats a chance
        char2_total = charactertotal(second_character) + random.randint(1, 6)   # character with lower fighting stat only gets 1 bonus but at least it cannot be a 0
        if char1_total > char2_total:   # compare the new total of both characters
            return first_character.name
        if char1_total < char2_total:
            return second_character.name
        else:
            return "It's a draw!"
    elif first_character.fighting < second_character.fighting:
        char1_total = charactertotal(first_character) + random.randint(1, 6)
        char2_total = charactertotal(second_character) + random.randint(0, 6) + random.randint(0, 6)
        if char1_total > char2_total:
            return first_character.name
        if char1_total < char2_total:
            return second_character.name
        else:
            return "It's a draw!"
    elif first_character.fighting == second_character.fighting:  # if both characters have equal fighting stat there is a random bonus given to each fighter that is added to their total
        char1_total = charactertotal(first_character) + random.randint(0, 6)
        char2_total = charactertotal(second_character) + random.randint(0, 6)
        if char1_total > char2_total:
            return first_character.name
        if char1_total < char2_total:
            return second_character.name
        else:
            return "It's a draw!"


def twovtwo(team1char1, team1char2, team2char1, team2char2):
    team1power = charactertotal(team1char1) + charactertotal(team1char2)    # grabbed total stats of both characters for team 1
    team2power = charactertotal(team2char1) + charactertotal(team2char2)    # grabbed total stats of both characters for team 2

    if team1power > team2power:  # apply bonuses to teams the same way we did for 1v1
        team1_total = team1power + random.randint(0, 6) + random.randint(0, 6)
        team2_total = team2power + random.randint(1, 6)
        if team1_total > team2_total:
            return 'Team 1'
        if team1_total < team2_total:
            return 'Team 2'
        else:
            return "It's a draw!"
    elif team1power < team2power:
        team1_total = team1power + random.randint(1, 6)
        team2_total = team2power + random.randint(0, 6) + random.randint(0, 6)
        if team1_total > team2_total:
            return 'Team 1'
        if team1_total < team2_total:
            return 'Team 2'
        else:
            return "It's a draw!"
    elif team1power == team2power:
        team1_total = team1power + random.randint + random.randint(0, 6)
        team2_total = team2power + random.randint + random.randint(0, 6)
        if team1_total > team2_total:
            return 'Team 1'
        if team1_total < team2_total:
            return 'Team 2'
        else:
            return "It's a draw!"

def freeforall(FFAcharacters):
    # Perform free for all battle
    # Pick a random 2 characters to fight in the list
    # Remove the looser in the list of active characters
    # Pick a random character in the list who hasn't fought yet
    # Evaluate for the winner and repeat until there is only 1 character left

    winner = 'winner'
    return winner


def versus():

    # Prompt for battle mode:
    mode = input('1. 1v1\n'
                 '2. 2v2\n'
                 '3. Free for all\n')

    if mode == '1':
        # Prompt for character name
        first_character = str(input('Enter a Superhero/Villain name: '))
        print()
        # find and store the first character
        first = findcharacter(first_character)

        # Prompt for second character
        second_character = str(input('Enter another Superhero/Villain name: '))
        print()

        second = findcharacter(second_character)
        # find and store the second character

        print('Now starting the battle!\n')
        time.sleep(1)
        winner = onevone(first, second)
        print(colors.green + 'The winner is... ' + winner + '!\n', colors.reset)
        time.sleep(2)
        start()

    elif mode == '2':
        print('2v2 mode selected')
        # Prompt for characters on team 1
        team1char1 = input('Enter first character for team 1: ')
        team1char1 = findcharacter(team1char1)
        team1char2 = input('Enter second character for team 1: ')
        team1char2 = findcharacter(team1char2)
        # Prompt for characters on team 2
        team2char1 = input('Enter first character for team 2: ')
        team2char1 = findcharacter(team2char1)
        team2char2 = input('Enter second character for team 2: ')
        team2char2 = findcharacter(team2char2)

        winningteam = twovtwo(team1char1, team1char2, team2char1, team2char2)
        print(colors.green + 'The winner is... ' + winningteam + '!\n', colors.reset)
        time.sleep(2)
        start()

    elif mode == '3':
        # Prompt for character select , store in a list and then prompt for more characters

        print('Free for all mode selected\n')
        ffacharacters = []
        selecting = True
        while selecting or len(ffacharacters) < 3:
            charname = input('Enter a character name for the free for all:\n')
            charname = findcharacter(charname)
            ffacharacters.append(charname)
            if len(ffacharacters) < 3:
                continue
            keepselecting = input('Select another character? Y/ N\n')
            if keepselecting.lower() in ['y', 'yes', 'sure']:
                selecting = True
            elif keepselecting.lower() in ['n', 'no', 'nope']:
                selecting = False

        # Start free for all
        winner = freeforall(ffacharacters)
        print('The winner is :' + winner)

    else:
        error_message()



def request_a_character(choice):
    with open("characters_to_add.txt", "a") as f:
        f.write(str(choice) + '\n')
        f.close()
    print(colors.green + 'Name has been added to the list! You can now go to '
                         'https://github.com/JordanLeich/Superhero-Villain-Index, fork the project, create '
                         'a pull request, and your text file with hero/villain names will be reviewed by '
                         'the developers.\n', colors.reset)
    time.sleep(3)
    start()


def start():  # sourcery no-metrics
    choice = int(input('''(1) Search the Superhero/Villain index
(2) Versus battles
(3) Extras
(4) Exit Program

Which option would you like to pick: '''))
    print()

    if choice == 1:
        choice = str(input('Enter a Superhero/Villain name: '))
        print()
        characters = create_characters()
        for c in characters:
            if choice.lower() == c.name.lower():
                Character.print_hero(c)
                time.sleep(2)
                choice = str(input('Would you like to view a photo of this Superhero/Villain (yes / no): '))
                print()
                if choice.lower() in ['y', 'yes', 'sure']:
                    Character.show_image(c)
                    time.sleep(1)
                    start()
                elif choice.lower() in ['n', 'no', 'nope']:
                    time.sleep(1)
                    start()
                else:
                    error_message()
        if choice.lower() != c.name.lower():
            print(colors.red + 'Superhero/Villain name not found!', colors.reset, '\n')
            time.sleep(2)
            write_to_text_choice = str(input(
                'Would you like to add this superhero/villain name to a text file so that the developers know who to add (yes / no): '))
            print()
            if write_to_text_choice.lower() in ['y', 'yes', 'sure']:
                request_a_character(choice)
            elif write_to_text_choice.lower() in ['n', 'no', 'nope']:
                start()
            else:
                error_message()
        else:
            error_message()
    elif choice == 2:
        versus()
    elif choice == 3:
        choice = int(input('''(1) View project releases/newest changes
(2) Credits
(3) Request a hero/villain to be added
(4) Return to main menu
(5) Exit Program

Which option would you like to pick: '''))
        print()
        if choice == 1:
            webbrowser.open('https://github.com/JordanLeich/Superhero-Index/releases')
            time.sleep(2)
            start()
        elif choice == 2:
            webbrowser.open('https://github.com/JordanLeich/Superhero-Index/graphs/contributors')
            time.sleep(2)
            start()
        elif choice == 3:
            choice = str(input('Enter the name of the hero/villain you would like added: '))
            print()
            characters = create_characters()
            for c in characters:
                if choice.lower() == c.name.lower():
                    print(colors.red + 'This hero/villain is already included in the index!\n', colors.reset)
                    time.sleep(1)
                    start()
            request_a_character(choice)
        elif choice == 4:
            start()
        elif choice == 5:
            sys.exit()
        else:
            error_message()
    elif choice == 4:
        sys.exit()
    else:
        error_message()


def error_message():
    print(colors.red + 'Error found!\n', colors.reset)
    time.sleep(2)
    start()


if __name__ == '__main__':
    start()
