"""Per-genre nouns and lines the mock beat graph interpolates into."""

FLAVORS: dict[str, dict] = {
    "scifi": {
        "you": "a systems engineer on the last inhabited ring of Station Helix",
        "place": "the vacuum-scarred docking spine of Station Helix",
        "place2": "Hydroponics Deck 4, where the grow-lights stutter in coded bursts",
        "place3": "the quarantine airlock over the moon's dark side",
        "climax_place": "HelixCorp's remote override booth",
        "item": "a cracked mag-key",
        "ally": "Irix, the station's half-broken AI",
        "threat": "the corporate kill-switch on life support",
        "hook": "a black-budget neural patch that rewrites worker loyalty",
        "inciting": (
            "Oxygen ticks down in red numerals. HelixCorp would rather vent the ring "
            "than let the patch leak to rival docks."
        ),
        "probe": (
            "The patch is not a rumor. It is already in the water recyclers, and every "
            "loyal badge on this deck will soon mean something uglier than employment."
        ),
        "complication": (
            "Irix admits the patch is in your bloodwork. Forty minutes until the rewrite "
            "locks. The consequence is already social: crews have started reporting each other."
        ),
        "crisis": (
            "The kill-switch can be stopped only from inside the venting chamber. "
            "Someone will freeze so the rest can breathe."
        ),
        "climax": (
            "A HelixCorp officer on a clean shuttle feed offers you a seat if you leave "
            "the others to the vacuum. No magic here—just policy with a countdown."
        ),
        "endings": {
            "grim": "The ring vents. Your last sensor log is a list of names the patch will never need.",
            "truth": "You dump the patch specs to every open channel. HelixCorp survives. So does the scandal. You do not get the shuttle.",
            "pyrrhic": "You smash the kill-switch with the mag-key and a broken arm. Air returns. Loyalty does not.",
            "hopeful": "Irix and the recyclers buy the ring twelve hours. Enough to wake the sleepers. Not enough to forgive HelixCorp.",
            "ambiguous": "You slip the shuttle and carry the patch sample. The ring's fate becomes someone else's memo.",
            "bittersweet": "The ring holds. The patch is in you. You remain yourself—for now—and that is the whole victory.",
        },
    },
    "horror": {
        "you": "a night janitor who stayed after the museum closed",
        "place": "the west wing of the municipal museum, lights already wrong",
        "place2": "the ethnography storeroom behind a door that should not open itself",
        "place3": "the boarded stairwell down to the unused bomb cellar",
        "climax_place": "the exhibit hall where the glass cases have fogged from the inside",
        "item": "a brass key tagged 'do not accession'",
        "ally": "the intern on the security radio, voice thinning",
        "threat": "whatever is wearing the old curator's smile",
        "hook": "a sealed collection that was never meant to be catalogued",
        "inciting": (
            "Something in the sealed wing knocks in a pattern you recognize as your own heartbeat, "
            "half a second late."
        ),
        "probe": (
            "The intern swears the curator went home. You find his coat still warm, and a second set of "
            "footsteps matching yours from inside the walls."
        ),
        "complication": (
            "The thing in the cellar knows your name. It does not need to chase you. The building "
            "folds hallways until you are already where it waits."
        ),
        "crisis": (
            "A display case shatters outward. What steps through is almost human, and the almost is the horror. "
            "You will not fully understand it, and it will not be put back."
        ),
        "climax": (
            "The intern begs you to lock them in with it so you can run. False safety was the gift. "
            "It is spent."
        ),
        "endings": {
            "grim": "Dawn finds the museum open. You are listed as missing. Something else clocks in for your shift.",
            "truth": "You burn the accession ledger. The town will call it arson. You will call it the only kindness left.",
            "pyrrhic": "You stop it with the brass key through what used to be an eye. It stops. So does the part of you that slept.",
            "hopeful": "You get the intern out. The cellar stays shut. Neither of you will work nights again.",
            "ambiguous": "You leave the lights on and walk into the parking lot. The knocking follows, politely, one beat behind.",
            "bittersweet": "The museum stands. You do not go back. Some damage is just the shape of memory now.",
        },
    },
    "noir_crime": {
        "you": "a private detective whose license is one unpaid favor from being pulp",
        "place": "a rain-slick alley behind the Marlowe Arms, neon drowning in gutter water",
        "place2": "a diner that serves coffee like an alibi",
        "place3": "the 12th Precinct's back stairs, where the good bulbs burned out on purpose",
        "climax_place": "a penthouse that smells like money and bleach",
        "item": "a pawn ticket wrapped around a .32 slug",
        "ally": "a waitress who hears more than she repeats",
        "threat": "a waterfront killing the papers already misspelled",
        "hook": "a civic 'redevelopment' fund that launders bodies as easily as cash",
        "inciting": (
            "A woman in a wet fur pays you to find her husband. He is already in the harbor. "
            "She knows. The job is to find out who needed him quiet."
        ),
        "probe": (
            "The husband was a clerk on the port authority. His last ledger line is a name the mayor "
            "shakes hands with on Sundays."
        ),
        "complication": (
            "The waitress slides you a photo: your client leaving the precinct with a captain's arm around her. "
            "The crime is not one bad man. It is the city's plumbing."
        ),
        "crisis": (
            "They offer you a fat envelope to lose the file. Keep it and you become the next harbor story. "
            "Your morality is not a speech. It is a price."
        ),
        "climax": (
            "In the penthouse the mayor's fixer explains, almost kindly, that the system is cleaner when "
            "people like you stay bought."
        ),
        "endings": {
            "grim": "The envelope is in your coat. The husband stays a typo. You drink like a man who knows the city's real name.",
            "truth": "You leak the ledger. A fall guy resigns. The fund changes letterheads. Nobody calls it justice, including you.",
            "pyrrhic": "You put the .32 on the table and walk the file to a reporter who will not live to see the Sunday edition.",
            "hopeful": "The waitress gets on a bus. You keep the file in a locker nobody has paid to open. It is a small, dirty mercy.",
            "ambiguous": "You take half the money and half the truth. The harbor keeps its dead. You keep your license.",
            "bittersweet": "The case closes. Nobody is happy. The city purrs, well-fed, and you are still the kind of person who notices.",
        },
    },
    "romcom": {
        "you": "a florist who talks to plants when deadlines talk back",
        "place": "a cramped shop two doors down from a rival cafe that steals your customers and, lately, your pulse",
        "place2": "the cafe's back patio during a disastrous shared catering gig",
        "place3": "city hall's marriage-license line, which you are absolutely not in for yourself",
        "climax_place": "the community hall before your best friend's wedding",
        "item": "a boutonniere with a note hidden in the stem",
        "ally": "Jordan, the cafe owner with foam art and worse timing",
        "threat": "a week of joint events that will either bankrupt you both or force an honest sentence",
        "hook": "a fake-dating pact to survive the wedding circuit",
        "inciting": (
            "Your best friend books both businesses for the wedding and announces you two 'already look like a couple.' "
            "Jordan laughs. You drop a vase. Chemistry, unfortunately, is present."
        ),
        "probe": (
            "The fake dates are going too well. A misunderstanding about whose mother called whom "
            "has you both pretending it was a joke."
        ),
        "complication": (
            "Jordan's lease and your shop's heat bill collide. Life goals: stay and fight the block, or take the safe job uptown. "
            "The romance is not a side plot. It is the plot, wearing florist ribbon."
        ),
        "crisis": (
            "At city hall you nearly say the wrong name to a clerk. The comedy dies. Honesty is suddenly the only gag left."
        ),
        "climax": (
            "The wedding is starting. Two leads, several disasters, and one chance to stop performing and mean it."
        ),
        "endings": {
            "grim": "You skip the reception. The flowers still go out. Hope does not. (Even here, the door stays unlocked tomorrow.)",
            "truth": "You tell Jordan everything in the coat closet. It is awkward, then kind, then a beginning.",
            "pyrrhic": "The wedding is perfect. You get the uptown job. You kiss in the rain and promise to try the distance. Trying counts.",
            "hopeful": "You stay on the block, merge the patio with the shop, and burn the fake-dating script. The ending is warm on purpose.",
            "ambiguous": "You dance once, badly, and agree to talk after the cake. It is not a vow. It is better than a bit.",
            "bittersweet": "The friend gets married. You and Jordan hold hands under the table like cowards and then, finally, like people.",
        },
    },
    "wuxian": {
        "you": "a young disciple of the Grey-Pine Sect with a cracked meridians rumor you have not earned yet",
        "place": "the mountain gate of Grey-Pine, mist catching on training posts",
        "place2": "the inner court where inner disciples drink tea like drawn blades",
        "place3": "the cliff arena above the jianghu road",
        "climax_place": "the ancestral hall of the Iron-Lotus Sect",
        "item": "a bamboo slip naming the Falling-Petal Sword Art",
        "ally": "your shixiong, who smiles like a warning",
        "threat": "a blood feud the elders call 'etiquette'",
        "hook": "Falling-Petal Sword Art, a technique that blooms only when the heart is divided",
        "inciting": (
            "Iron-Lotus has demanded a life for a slight. Grey-Pine's hierarchy is clear: outer disciples bleed first. "
            "Your name is already on the challenge board."
        ),
        "probe": (
            "The bamboo slip is real. Falling-Petal requires you to choose between the sect's face and the person "
            "you were ordered not to love."
        ),
        "complication": (
            "Your shixiong is promised to an Iron-Lotus heir. Loyalty to the mountain and the pulse in your wrist "
            "cannot occupy the same stance."
        ),
        "crisis": (
            "The cliff arena does not care about your feelings. Elders on both sides sit like millstones. "
            "A named art must be shown, or Grey-Pine is meat."
        ),
        "climax": (
            "In the ancestral hall you may kneel, strike, or walk away from the jianghu's accounting. "
            "Honor is a blade with two handles."
        ),
        "endings": {
            "grim": "You win the exchange and lose the person. The sect records a victory. The mountain is very quiet.",
            "truth": "You name the feud a vanity and refuse the blood. Both sects call it shame. The road calls it a beginning.",
            "pyrrhic": "Falling-Petal opens. Iron-Lotus yields. Your meridians scream. Power always invoices the body.",
            "hopeful": "You and your shixiong leave under a stolen dusk, technique intact, hierarchy behind you like shed skin.",
            "ambiguous": "You bow to both halls and take a wandering name. The jianghu will decide later what that meant.",
            "bittersweet": "The feud pauses. You remain Grey-Pine. The heart remains a problem the manuals do not index.",
        },
    },
    "war_story": {
        "you": "a medic attached to a rifle company that has already spent its luck",
        "place": "a ruined school on the edge of an occupied town, desks still in rows",
        "place2": "a cellar aid station that smells like iron and wet wool",
        "place3": "the crossroads under the water tower, where the last assault stalled",
        "climax_place": "the command post in the mayor's kitchen",
        "item": "a field kit with more gauze than morphine",
        "ally": "a corporal who keeps other people's letters dry",
        "threat": "an order to retake the crossroads at dawn",
        "hook": "a bombardment that turned a street into a lesson about distance",
        "inciting": (
            "The wounded keep arriving. The town is not a backdrop; it is a body. Dawn's attack will write more of them."
        ),
        "probe": (
            "Civilians are still in the basements. Command wants the tower. You can hear both truths from the same stairwell."
        ),
        "complication": (
            "The corporal asks you to mark a man 'unfit' so he is not thrown back into the meat. "
            "Obedience and care no longer fit in one kit."
        ),
        "crisis": (
            "The assault goes badly. You work in mud while the water tower burns. Courage here is just staying. "
            "Trauma is already taking attendance."
        ),
        "climax": (
            "An officer wants you to leave the civilians and move with the surviving squad. "
            "There is no glamorous version of this hour."
        ),
        "endings": {
            "grim": "The crossroads is taken. Your company is a roster of absences. You pack the kit because that is what is left of duty.",
            "truth": "You file the true casualty numbers. Someone will bury them. The town knows anyway.",
            "pyrrhic": "You drag three people out and lose the corporal's letters in the mud. Survival is not a parade.",
            "hopeful": "The attack is delayed. A few basements empty toward the river. You call that a win in a voice that does not believe you.",
            "ambiguous": "You follow the squad and do not look back at the school. After the war, looking back will be the rest of your work.",
            "bittersweet": "Dawn ends. Some of you remain. Nobody here will ever describe it as clean.",
        },
    },
    "urban_fantasy": {
        "you": "a barista with a leftover spark in the blood and rent due Friday",
        "place": "a 24-hour subway mezzanine where the fluorescent lights refuse one corner",
        "place2": "the staff alley behind your cafe, dumpsters and a thin place in the world",
        "place3": "a hidden court above a laundromat, neon saints in the windows",
        "climax_place": "the inbound platform at 3:12 a.m., when the last train is not a train",
        "item": "a MetroCard that opens doors the MTA did not build",
        "ally": "a night-shift cop who pretends not to see the horns",
        "threat": "a debt-collector from the hidden borough",
        "hook": "a glamour that lets monsters use turnstiles like commuters",
        "inciting": (
            "A thing in a good coat asks for oat milk and your true name. The cafe's card reader coughs out runes. "
            "Normal life just got a second job."
        ),
        "probe": (
            "The hidden court says you inherited a crossing-guard contract. Your boss still expects you on the opening shift."
        ),
        "complication": (
            "If you skip the magical duty, something rides the morning crowd. If you skip work, you lose the apartment "
            "that keeps you human-shaped."
        ),
        "crisis": (
            "The debt-collector is already in the mezzanine, smiling with too many commuters' faces. "
            "Phones still work. Magic does not care."
        ),
        "climax": (
            "The last train is a mouth. You can feed it a name, a city, or yourself. The mundane and the uncanny "
            "are sharing one platform."
        ),
        "endings": {
            "grim": "You clock in on time. The crossing fails. The city files it as a delay. You taste iron in the espresso for weeks.",
            "truth": "You out the court on a late-night blog nobody believes. The cop believes you. That is almost enough.",
            "pyrrhic": "You close the crossing with the MetroCard and a burned-out spark. Rent will be a problem. Breathing is not.",
            "hopeful": "You negotiate a night-shift treaty: cafe until ten, threshold until dawn. Two worlds, one terrible calendar.",
            "ambiguous": "You give a false name to the train. It leaves. You keep your job. Something keeps your scent.",
            "bittersweet": "The mezzanine is ordinary at rush hour. You are not. You pour coffee and watch the thin corner like a second register.",
        },
    },
    "apocalypse": {
        "you": "a junior climatologist pulled into a bunker that still uses clipboards",
        "place": "a glass observation deck over a city whose sky has turned the color of a bruise",
        "place2": "the evacuation railhead, already a riot of headlights",
        "place3": "the bunker map room, where the red zones eat the coast in real time",
        "climax_place": "the antenna roof as the sirens braid into one note",
        "item": "a satellite token that can retarget one last broadcast",
        "ally": "a logistics officer who keeps counting heads out loud",
        "threat": "a cascade failure: heat, then grid, then the reservoirs blooming toxic",
        "hook": "a six-hour window before the downwind cities are unlivable",
        "inciting": (
            "This is not a metaphor. The reservoirs are turning. Time is a number on the wall and it is running out "
            "for more people than you can see from here."
        ),
        "probe": (
            "You can save a corridor of hospitals or a corridor of reservoirs, not both. The officer wants a signature. "
            "The signature is a massacre either way."
        ),
        "complication": (
            "Your sister's district is in the hospital corridor. Policy forbids you from saying so. "
            "The catastrophe is global. Your hands are still local."
        ),
        "crisis": (
            "The railhead will collapse in ninety minutes. Someone has to stay and keep the model honest "
            "while the rest run."
        ),
        "climax": (
            "The last broadcast can carry one instruction: flee inland, or shelter in the hospital belt. "
            "Millions will hear whichever sentence you choose."
        ),
        "endings": {
            "grim": "You hesitate. Both corridors fail in different hours. The model was right. Being right is not a shelter.",
            "truth": "You tell the whole truth on the broadcast, ugly numbers included. Panic is a cost. Lies would have been a bigger one.",
            "pyrrhic": "You pick the hospitals. The reservoirs die. Your sister lives long enough to know what you did.",
            "hopeful": "The token retargets just enough. Not everyone. Enough that tomorrow still has a census.",
            "ambiguous": "You stay on the roof and send both messages in pieces. History will call it noise. A few convoys will call it luck.",
            "bittersweet": "The window closes. Some trains left. You have to live with the map you drew, not the one you wanted.",
        },
    },
    "postapocaliptic": {
        "you": "a scavenger who still remembers grocery stores as a kind of myth",
        "place": "the skeleton of an interstate overpass, tarps and cooking smoke underneath",
        "place2": "a trading post in a dead big-box store, paint still promising savings",
        "place3": "the settlement cistern, guarded like a church",
        "climax_place": "the rusted water-treatment plant the old world left like a dare",
        "item": "a hand-pumped filter that might last a season",
        "ally": "Mira, who runs the post's board of debts",
        "threat": "the Cistern Kings, who tax water and call it order",
        "hook": "a dry month and a rumor of a working pump in the plant",
        "inciting": (
            "The fall already happened—years back, when the grid went and stayed gone. Now the cistern is low, "
            "and every faction's law is thirst."
        ),
        "probe": (
            "Mira will stake you a filter if you bring plant parts. The Kings will break fingers for less. "
            "Rebuild is a word people use when they have not hauled water."
        ),
        "complication": (
            "The plant still holds a poison the old world named in a language of warning labels. "
            "Fix the pump wrong and the settlement drinks a second ending."
        ),
        "crisis": (
            "Kings at the gate, kids at the cistern. You can cut a deal, cut a hose, or cut and run with the filter."
        ),
        "climax": (
            "Inside the plant the pump groans like it remembers cities. No restoration of the world—only a local, "
            "expensive chance at water that does not belong to kings."
        ),
        "endings": {
            "grim": "The Kings keep the plant. You keep your skin. The settlement learns a new tax. The old world stays dead.",
            "truth": "You mark the poison lines in paint the kids can read. Knowledge is salvage. It will not make anyone young.",
            "pyrrhic": "The pump works. The Kings burn the post. Mira lives. The filter does not.",
            "hopeful": "A trickle hits the cistern that is not a King's. Hope here is a cup, not a flag.",
            "ambiguous": "You take the filter west. Someone else's thirst becomes a story you tell if you make it.",
            "bittersweet": "Water, for now. The overpass still groans in the wind. Nobody is going back to before.",
        },
    },
    "cold_war_spy_setting": {
        "you": "a field agent with a legend that is starting to itch",
        "place": "a smoky bar two blocks from a checkpoint, 1973 if anyone asks",
        "place2": "a safe house with a radio that clicks like a guilty conscience",
        "place3": "the embassy's basement archive, where the good lies are filed",
        "climax_place": "a night train toward a border that pretends to be geography",
        "item": "a microfilm in a cigarette pack",
        "ally": "your handler, whose smile is a tradecraft problem",
        "threat": "a mole hunt that will burn someone innocent if it cannot burn the guilty",
        "hook": "a dead drop that arrived a day early, which is how graves get dug",
        "inciting": (
            "East and West want the same list of names. You are meant to photograph it, not believe it. "
            "Belief is how assets become obituaries."
        ),
        "probe": (
            "The dead drop is real. So is the surveillance. Someone on your side already knew the time. "
            "Tradecraft: you do not ask the radio; you watch who flinches when it hisses."
        ),
        "complication": (
            "The handler might be the mole. The opposition might be offering you a cleaner legend. "
            "Cause, country, and the person who makes your coffee are no longer aligned."
        ),
        "crisis": (
            "A checkpoint sergeant wants a look at your papers while the microfilm warms in your coat. "
            "No rooftop ballets. Just sweat and a stamp."
        ),
        "climax": (
            "On the night train you can pass the film west, east, or into the river. "
            "Whoever you trust will live with the names. Whoever you don't, also."
        ),
        "endings": {
            "grim": "The mole hunt finds you convenient. The list goes to the wrong desk. You get a medal in a closed room.",
            "truth": "You burn the film and keep the names in your head. Neither bloc likes that. Ambiguity was the job.",
            "pyrrhic": "You expose the handler. The operation collapses. A few assets vanish who did not deserve to.",
            "hopeful": "The film reaches a desk that will use it to warn, not to hang. You doubt it. You still sleep an hour.",
            "ambiguous": "You give each side a different half. The border stays a border. You stay employed. That is not the same as safe.",
            "bittersweet": "The train crosses. You do not. Someone else carries the pack. Victory, if any, will be footnoted.",
        },
    },
}


BEAT_ORDER = ["opening", "probe", "complication", "crisis", "climax", "ending"]

VISUAL_BY_BEAT = {
    "opening": "threshold",
    "probe": "interior_night",
    "complication": "alley",
    "crisis": "exterior_dawn",
    "climax": "climax",
    "ending": "ending",
}

LOCATION_BY_BEAT = {
    "opening": "place",
    "probe": "place2",
    "complication": "place2",
    "crisis": "place3",
    "climax": "climax_place",
    "ending": "climax_place",
}
