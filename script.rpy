# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define narrator = Character(window_background="gui/textbox_narration.png", what_font='courbd.ttf', what_size=22,  color='#000000', what_color='#000000')
define op = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5)
define n = Character("NAXILI", color='#FFFFFF', image="naxili", window_background="gui/textbox_olive.png", who_outlines=[ (4, "#658200") ],)
define ht = Character("HEFAIS", color='#FFFFFF', image="hefais", window_background="gui/textbox_bronze.png", who_outlines=[ (4, "#a15000") ],)

### MUSIC INITIALIZING GOES HERE ###
define audio.hefaistheme = "music/Gordian.mp3"
define audio.naxilitheme = "music/Sunstone.wav"
define audio.boom = "music/boom.wav" #CREDIT: https://freesound.org/people/ryansnook/sounds/110115/
define audio.win = "music/victory_jingle.mp3"
define audio.lose = "music/game_over.mp3"

### IMAGE INITIALIZING GOES HERE ###
image naxili happy = "images/naxili_happy.png"
image naxili angry = "images/naxili_angry.png"
image naxili annoy = "images/naxili_irritated.png"
image naxili blush = "images/naxili_blush.png"
image naxili neutral = "images/naxili_neutral.png"
image naxili rage = "images/naxili_rage.png"
image naxili uncomf = "images/naxili_uncomfortable.png"

image naxili ghappy = "images/naxili_g_happy.png"
image naxili gangry = "images/naxili_g_angry.png"
image naxili gannoy = "images/naxili_g_irritated.png"
image naxili gneutral = "images/naxili_g_neutral.png"
image naxili grage = "images/naxili_g_rage.png"
image naxili guncomf = "images/naxili_g_uncomfortable.png"

image hefais happy = "images/hef_happy.png"
image hefais annoy = "images/hef_annoy.png"
image hefais angry = "images/hef_angry.png"
image hefais sweat = "images/hef_sweat.png"
image hefais fake = "images/hef_fake.png"
image hefais shock = "images/hef_shock.png"
image hefais wistful = "images/hef_sad.png"
image hefais nervous = "images/hef_nervous.png"
image hefais angry2 = "images/hef_angry.png"

image bg naxili_good = "images/naxili_good.png"
image bg naxili_bad1 = "images/naxili_bad_1.png" #axe death
image bg naxili_bad2 = "images/naxili_bad_2.png" #strangled

image bg hef_good = "images/hef_good.png"
image bg hef_bad1 = "images/hef_bad_1.png"
image bg hef_bad2 = "images/hef_bad_2.png"

image bg alternia = "images/background1.png"
image bg alternia2 = "images/background4.png"
image bg alternia3 = "images/background2.png"
image bg alternia4 = "images/background3.png"

image bg broken = "images/broken_hive.png"

image bg desert night = Image("images/desertnight.png", ypos=730)
image bg spaceship = Image("images/background_spaceship.png")

image bg outskirts = Image("images/tyzias_townoutskirts.png", ypos=720) 
image bg bookhive = Image("images/tyzias_bookhive.png", ypos=720)

image bg trainstation = Image("images/Trainstation.png", ypos=720)
image bg forest = Image("images/forest.png", ypos=720)
image bg clownchurch = Image("images/clown_church.png", ypos=720)

image bg limo = Image("images/bg_limo.png", ypos=720)

image bg alley = "images/alley.png"
image bg cafe = Image("images/Coffee shop.png", ypos=730)  
image bg rain = Image("images/neighborhood_rain_final.png", ypos=720)
image bg junkyard = Image("images/junkyard_final.png",ypos=720)
image bg scuttlebuggy = Image("images/scuttlebuggyint_final.png", ypos=720)
image bg neighborhood = Image("images/bg_neighborhood3.png")


image bg galekhhive = Image("images/Galekh_Hive_Ext.png", ypos=720)
image bg galekhstudy = Image("images/Galekh_Study_Int.png", ypos=720)

image bg stelsahive = Image("images/stelsa_office_final.png", ypos=720)

image bg undergrowth1 = Image("images/BG_karako_undergrowth_1.png",ypos=720)
image bg undergrowth2 = Image("images/BG_karako_undergrowth_2.png",ypos=720)

image field2 = Image("images/field-2-nolight.png",ypos=720, xanchor=640, yanchor=720)
image field2light = Image("images/field-2.png",ypos=720, xanchor=640, yanchor=720)

image bg sewer = "images/sewer.png"

image bg cave = Image("images/bronya_cave.png", ypos=730)
image bg hideout = Image("images/yourhive.png", ypos=720)

image theatre = "images/theatre.png"

image fog = "images/fog.png"

image bg black = "images/blackcover.png"

image bloodsplatter = "images/bloodborder.png"

image bloodsplatterred = "images/bloodborderred.png"



style outlined:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    color "FFFF00"
    bold True
    
style friend:
    outlines [ (absolute(2), "#FF00FF", absolute(1), absolute(1)) ]
    color "FFFF00"
    font "courbd.ttf"
    size 72
    
style choice_button_text:
    color "0000FF"
    font "courbd.ttf"
    
    
define quickmove = PushMove(0.2, "pushleft")
define quickfade = Dissolve(0.1)

#####################################

transform wiggle:
    rotate 0
    ypos -250
    
    on hover:
        linear .1 rotate -2
        linear .1 rotate 0
        linear .1 rotate 2
        linear .1 rotate 0

transform bounce:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    
transform bouncetwice:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    pause(0.2)
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    
transform quickbouncetwice:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform nod:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    
transform nodtwice:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause 0.5
    easeout 0.15 ypos 742
    linear 0.15 ypos 730
    
transform quicknodtwice:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause(0.1)
    easeout 0.15 ypos 742
    linear 0.15 ypos 730

transform slownod:
    ypos 730
    easeout 0.3 ypos 742
    pause 0.5
    linear 0.2 ypos 730

transform slowishnod:
    ypos 730
    easeout 0.27 ypos 742
    linear 0.2 ypos 730
    
transform twitch:
    ypos 730 xpos 640
    easein 0.06 ypos 736 xpos 644
    linear 0.06 ypos 730 xpos 640
    
transform shudder:
    
    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat 4
    
transform lowered:
    ypos 730
    linear 0.75 ypos 765

transform loweredtodefault:
    ypos 765
    linear 0.3 ypos 730

transform loweredpos:
    ypos 765
    
transform loweredbrief:
    ypos 730
    pause 0.05
    linear 0.75 ypos 765
    pause 1.8
    linear 1.35 ypos 730

transform loweredbounce:
    ypos 765
    easeout 0.12 ypos 751
    linear 0.12 ypos 765

transform smalllower:
    ypos 730
    linear 0.15 ypos 736

transform smalllowertodefault:
    ypos 736
    linear 0.14 ypos 730

transform sitting:
    ypos 765
    linear 0.75 ypos 800
    
transform leftsitting:
    xpos 360 ypos 850

transform rightsitting:
    xpos 960 ypos 850

transform sitsigh:
    ypos 850 xpos 640
    easein 0.4 ypos 845
    easeout 0.6 ypos 850

transform sittingnod:
    ypos 850 xpos 640
    easein 0.4 ypos 845
    easeout 0.6 ypos 850
    
transform bouncing:
    ypos 730
    linear 0.1 ypos 720
    linear 0.1 ypos 730
    repeat
    
transform shaking:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730
    repeat
    
transform shakes:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730
    repeat 3
    
transform shuddering:
    
    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat

transform sigh:
    ypos 730
    easein 0.4 ypos 725
    easeout 0.6 ypos 730

transform breathe:
    ypos 730
    easein 1 ypos 720
    easeout 1.1 ypos 730

transform breathein:
    ypos 730
    easein 1 ypos 720

transform breatheout:
    ypos 720
    easeout 1.1 ypos 730

transform breathing:
    easein 1 ypos 720
    easeout 1.1 ypos 730
    pause(1.0)
    repeat

transform outofbreath:
    ypos 730
    easein 0.5 ypos 720
    easeout 0.6 ypos 730
    pause(0.5)
    easein 0.5 ypos 720
    easeout 0.6 ypos 730
    pause(0.4)
    repeat

transform speaking:
    easein 0.1 zoom 1.01
    easein 0.1 zoom 1.01

transform stopspeaking:
    easein 0.1 zoom 1

transform speakbounce:
    parallel:
        easein 0.1 zoom 1.01
    parallel:
        ypos 730
        easeout 0.12 ypos 716
        linear 0.12 ypos 730

transform speaknod:
    parallel:
        easein 0.1 zoom 1.01
    parallel:
        ypos 730
        easeout 0.12 ypos 742
        linear 0.12 ypos 730

transform driving:
    ypos 720
    linear 0.07 ypos 722
    linear 0.07 ypos 720
    repeat

transform highbounce:
    ypos 730
    easeout 0.12 ypos 690
    linear 0.12 ypos 730

transform passenger:
    ypos 730 xpos 900 zoom 1.2

transform flipped:
    xzoom -1.0

transform fallen:
    xpos 640 ypos 1000

transform leftfallen:
    xpos 360 ypos 1000

#Quickly push sprite to side of screen    
transform shoveright:
    
    linear 0.1 xpos 960
    
transform shoveleft:
    
    xpos 640
    linear 0.1 xpos 320
    
transform shoveoffleft:
    
    linear 0.1 xpos -320
    
#Quickly push sprite to default position, from offscreen bottom
transform shoveup:
    xpos 640 ypos 1440
    linear 0.1 ypos 730
    
## UNCOMMON TRANSFORMS ##

transform middle:
    
    ypos 730 xpos 640

#Modified left position for sprites with 1280 width
transform left1280:
    
    ypos 730 xpos 360
    
transform farleft1280:
    
    ypos 730 xpos 180

transform halfleft1280:
    
    ypos 730 xpos 500 

#Modified right position for sprites with 1280 width
transform right1280:
    
    ypos 730 xpos 960
    
transform farright1280:
    
    ypos 730 xpos 1080
    
#Modified right position for sprites with 1280 width
transform halfright1280:
    
    ypos 730 xpos 780
    
#Brings the character in closer
transform moveclose:
    ypos 730 zoom 1.0
    easeout 0.6 ypos 815 zoom 1.2
    
#Moves them back
transform moveaway:
    ypos 815 zoom 1.2
    easeout 0.45 ypos 730 zoom 1.0
    
transform quickhug:
    ypos 730 xpos 640 zoom 1.0
    easeout 0.7 ypos 640 xpos 320 zoom 1.5
    pause 1.9
    ypos 640 xpos 320 zoom 1.5
    easeout 0.6 ypos 730 xpos 640 zoom 1.0
    
transform kicking:
    ypos 730
    easeout 0.09 ypos 716 xalign 0.62
    linear 0.09 ypos 730 xalign 0.5
    pause 0.04
    easeout 0.09 ypos 716 xalign 0.62
    linear 0.09 ypos 730 xalign 0.5
    
transform cornerbounce:
    ypos 734
    easeout 0.12 ypos 720
    linear 0.12 ypos 734
    
transform slowbounce:
    ypos 730
    easeout 0.15 ypos 720
    linear 0.15 ypos 730

transform slowbouncing:
    ypos 730
    linear 0.13 ypos 725
    linear 0.13 ypos 730
    repeat
    
transform slowerbounce:
    ypos 730
    easeout 0.1 ypos 724
    linear 0.1 ypos 730

transform slowerbouncing:
    ypos 730
    easein 0.3 ypos 724
    linear 0.3 ypos 730
    repeat

transform pausebouncing:
    ypos 730
    linear 0.1 ypos 720
    linear 0.1 ypos 730
    pause 0.5
    repeat

transform brush:
    xpos 640
    linear 0.1 xpos 635
    linear 0.1 xpos 640

transform brushright:
    xpos 640
    linear 0.1 xpos 645
    linear 0.1 xpos 640

transform leanin:
    ypos 730
    easein 0.2 zoom 1.05 ypos 750

transform leanout:
    ypos 750
    easein 0.2 zoom 1.0 ypos 730

#Sets zoom/position back to default
transform defaultzoom:
    easeout 0.1 zoom 1 ypos 730 

transform typing:
    ypos 730
    linear 0.18 ypos 733
    linear 0.17 ypos 730
    pause(0.1)
    linear 0.12  ypos 732
    linear 0.12 ypos 730
    linear 0.14  ypos 732
    linear 0.13 ypos 730
    ypos 730
    repeat

transform search:
    ypos 730
    easeout 0.16 ypos 742
    linear 0.16 ypos 730
    pause 0.3
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause 0.06
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause 0.8
    easeout 0.1 ypos 742
    linear 0.1 ypos 730
    pause 0.4
    easeout 0.12 ypos 742
    linear 0.12 ypos 730
    pause 0.2
    repeat

transform searcharound:
    xpos 640
    easeout 0.32 xpos 580
    easeout 0.3 xpos 700
    easeout 0.28 xpos 620
    easeout 0.26 xpos 690
    easeout 0.2 xpos 640
    xpos 640

transform gesture:
    ypos 730 xpos 640
    easeout 0.15 xpos 620
    easeout 0.15 xpos 660
    easeout 0.1 xpos 640
    xpos 640

transform holdingup:
    easein 0.60 zoom 1.6 ypos 700
    easeout 0.45 zoom 2.2 ypos 1250
    
transform setdown:
    easein 0.45 zoom 1.6 ypos 825
    easeout 0.60 zoom 1.0 ypos 730
    
transform dungeon:
    ypos 734
    linear 0.5 xalign -0.12 zoom 0.75
    
transform bloodoverlay:
    zoom 1.25 rotate 65 yalign 0.42 xalign 0.48
    
transform sweepleft:
    linear 0.66 xalign -1.50
    
transform sweepright:
    linear 0.66 xalign 2.00
    
transform hugincoming:
    
    easeout 0.66 zoom 1.15
    pause 0.25
    easeout 0.66 zoom 1.0

transform hug:
    ypos 730
    easeout 1 zoom 1.75 ypos 1000
    
transform endhug:
    
    easein 0.33 zoom 1.0 ypos 730
    
transform closeup:
    easein 1.5 zoom 1.75 ypos 1025
    
transform dogzoom1:
    easein 0.5 zoom 1.9 ypos 1075
    
transform dogzoom2:
    easein 0.5 zoom 2.05 ypos 1125
    
transform dogzoom3:
    easein 0.5 zoom 2.20 ypos 1175
    
transform dogzoom4:
    easein 0.5 zoom 2.35 ypos 1225
    
transform dogzoom5:
    easein 0.5 zoom 2.5 ypos 1275
    
transform dogzoom6:
    easein 0.5 zoom 2.65 ypos 1325
    
transform dogunzoom:
    easeout 0.1 zoom 1.0 ypos 730
    
transform dogchoke:
    
    yalign 1.0 ypos 730
    easeout 0.15 ypos 760
    pause 0.2
    linear 0.03 ypos 756
    linear 0.03 ypos 760
    linear 0.03 ypos 756
    linear 0.03 ypos 760
    linear 0.03 ypos 756
    easein 0.35 ypos 770
    pause 0.15
    linear 0.08 ypos 740
    easein 0.1 ypos 730
    pause 0.3
    repeat
    
transform diemendies:
    
    linear 0.04 ypos 730
    easeout 0.8 ypos 500
    pause 0.1
    linear 0.08 rotate 180
    easein 0.35 ypos 1640
    
transform dogagony:
    xalign 0.5 ypos 730
    easein 0.25 xalign 0.45 ypos 740
    easeout 0.25 xalign 0.55 ypos 750
    easeout 0.25 xalign 0.45 ypos 760
    easeout 0.25 xalign 0.55 ypos 770
    easeout 0.25 xalign 0.45 ypos 780
    easeout 0.25 xalign 0.55 ypos 790
    easeout 0.25 xalign 0.45 ypos 800
    easein 0.25 xalign 0.5 ypos 810
    
transform rumbling:
    
    ypos 730
    linear 0.1 ypos 728
    linear 0.1 ypos 732
    repeat
    
transform sludgeanim:
    
    ypos 730
    easein 0.4 ypos 775
    pause 0.2
    easein 0.4 ypos 730
    pause 0.2
    repeat
    
transform drownanim:
    
    ypos 730
    easein 0.45 ypos 775
    pause 0.25
    easein 0.35 ypos 730
    pause 0.25
    repeat
    
transform sludgebegone:
    
    linear 1.8 ypos 1440
    
transform goatpet:
    ypos 730 xpos 360
    easeout 0.2 xpos 340 ypos 734
    easeout 0.2 xpos 360 ypos 730

transform lookaround:
    
    xalign 0.5
    linear 0.6 xalign 0.0
    pause 1.2
    linear 0.3 xalign 0.5
    pause 1.2
    linear 0.3 xalign 1.0
    pause 1.2
    linear 0.6 xalign 0.5
    
transform entranceleft:
    yalign 1.0
    xpos -1000
    linear 1.2 xpos 0
    
transform entranceright:
    yalign 1.0
    xpos 1000
    linear 1.2 xpos 0
    
transform menumove:
    
    xpos 20
    
    on hover:
        linear .25 xpos 50
        
    on idle:
        linear .25 xpos 20
        
transform wiggle:
    
    rotate 0
    ypos -250
    
    on hover:
        linear .1 rotate -2
        linear .1 rotate 0
        linear .1 rotate 2
        linear .1 rotate 0
    
python:
    
    import os
    import os.path

# The game starts here.

label start:

    $ renpy.block_rollback()
    
    $ main_menu = False
    
    show image "gui/game_menu.png"
    
    window hide
    
    scene black with Dissolve(1.5)
    
    op "Here you are, on Alternia."
    op "After a wacky series of events, you've found yourself stuck on this strange planet, full of odd colors and a sun that could scorch you flat."
    op "But it's not so bad! After all, you've found something here that keeps you running strong:"
    op "{size=80}{=friend}FRIENDSHIP.{/=friend}{/size}"
    op "When trouble is afoot, you can never go wrong punching it right in the snout with a buddy!"
    op "In fact, speaking of buddies... You're feeling awfully chummy tonight in particular. Why not make some new pals?"

    call screen troll_select1 with Dissolve(1.0)
    
    with Pause(0.25)

    return

label naxili:
    $ renpy.block_rollback()

    scene black with Dissolve(1.0)
    
    scene bg alternia with dissolve
    
    $ quick_menu = True
    stop music fadeout 2.0
    "The air is crisp and clean, and for the first time in a while, no one seems to be out and about in your neck of the woods. For now, you just enjoy the peace and quiet as you trek by a handful of colorful hives."
    "You start to let your mind wander while wondering how some of these towering buildings are actually made when something gets caught up under your feet."
    scene bg alternia at vpunch
    "Oof. You manage to catch yourself mid-fall, rolling over so you can get a proper look at whatever it was that just tripped you up."
    "On the sidewalk sits one of those strange white creatures, about the size of an Earth dog."
    "But rather than a fluffy barkfriend, this thing embodies more of a large, silly looking salamander, with a wide, bulbous head and two big, bulging eyes."
    "It bleps at you in what seems to be a friendly manner, and seems relatively unharmed. Hey, maybe this can be the new friend you're so desperate for?"
    "You manage to stand and pick the large salamander up into your arms; it's surprisingly light for its size."
    "It seems to catch your drift and ends up slithering up your back and perching on your shoulders like some sort of awkward shawl."
    "Now that you think about it, aren't these monochromatic monsters usually parental units for trolls? Is this someone's mom you've just tripped over and picked up?"
    "Now that's a weird thought to process."
    scene bg alternia at hpunch
    play sound boom
    #explosion sfx
    scene bg alternia with flash
    "A flash of instantaneous light is the only brief warning before the side of the hive closest to you explodes, pieces of wall and furniture going flying into the lawnring below."
    "Some of the aftermath comes flying in your direction, and you barely manage to dodge some flaming bits of table."
    "The salamander on your shoulders seems nonplussed by the development and has taken to hiss-shrieking directly into your right ear."
    window hide
    play music naxilitheme fadein 1.0
    n "CØUGH-- CØUGH--"
    "Someone's stumbling out of the gaping hole of the hive! You hurry over, careful to keep a clear radius around anything that seems like it might spontaneously combust where it sits."
    show naxili gannoy with moveinbottom
    "She quickly scrubs ash and dirt from her face with the back of her forearm, grumbling loudly as she kicks over some debris and looks over what's left of her hive."
    "She barely acknowledges your presence when you get close, but you figure you'd ask her if she'd like a helping hand with the clean-up all the same."
    n gangry "Gurgh-- What?"
    n gannoy "I mean, I'm nøt gønna turn døwn free help, but frankly..."
    n "What øn Alternia are yøu suppøsed tø be?"
    "You introduce yourself to the troll, briefly explaining your species and making sure to mention that friendship is like, a big part of human culture."
    "You also mention that, hey, regardless of species, who doesn't flourish from a little bit of platonic social bonding?"
    n "...Yøu have søme weird fucking priørities, human. But øk. I'll bite. Especially if it means free sanitation vassal services."
    n gneutral "My name's Naxili Miiace by the way."
    n gannoy "I am specifically telling yøu this sø yøu støp calling me weird vague terms like \"friend\"."
    "You wonder aloud why you aren't allowed to call her \"friend\" anymore, and if \"pal\" or \"buddy\" is still on the table."
    n "Because we literally just met? And nø, nø øther nicknames!"
    "She finally takes her safety glasses off, unceremoniously wiping the dirt on the lense onto her dark grey shirt. In the middle of her safety-scrubbing, she finally gives you a proper once over."
    n angry "Is that--"
    n "Augh!"
    "Naxili runs over, shoving her safety glasses back over her face and using her free hands to grab the salamander who has been politely chilling on your back this whole time."
    "Now though, as Naxili pulls, the salamander seems to be clinging to you deperately with its sticky lizard grasp."
    "And it's kind of starting to hurt?"
    n gannoy "Let {i}gø{/i} øf the alien, you weirdø!"
    "Through the pain, you manage to eek out that you're not stuck to this salamander intentionally."
    n "What? Nø, nøt yøu dipshit, I meant my gøød-før-nøthing lusus. Yes, yøu, yøu sørry sack of biømatter. Let gø!"
    "The salamander lets out an indignant huff before a series of small {i}pops{/i} precedes Naxili reeling backwards, lusus in hand."
    "She quickly puts it down on the ground, and the creature slithers across the lawnring and into the large hole in the side of Naxili's hive."
    n gneutral "Sørry abøut that. She can be clingy."
    "You assure her it's no problem at all. Other than the painful yanking and the hissing, her lusus was actually quite nice."
    n "If you enjøy her sø much, maybe yøu can be her new ward."
    "It's hard to tell if she's joking, but she's already heading back inside, stepping nonchalantly over rubble and debris. You do your best to follow suit."
    show bg broken with wipeleft
    "Inside seems like your average hive, except for the fact that half of the kitchen area seems to be missing now."
    "There also seems to be an absurd amount of glass shards scattered about the countertops. Off to the side, a bunsen burner is tipped over and seems to still be on in the kitchen sink."
    "Naxili moves to turn the burner off, then turns to you."
    n "Well, I'd øffer yøu sømething tø drink beføre we get started, but, uh. Yøu knøw."
    "Right. Whatever was offerable was probably blown to bits. Hey, maybe you guys could go shopping after you're done cleaning! Pick up some groceries and stuff. That's always a fun bonding activity!"
    n gannoy "Øk, døn't push yøur luck, first øf all."
    n gneutral "Secønd of all, bøld øf yøu tø suggest we can get all of this cleaned up before mørning."
    "She gestures around herself. It is kind of a lot, but you're ready to roll up your metaphorical sleeves. Nothing that some teamwork and elbow grease can't fix!"
    n gannoy "Yøu are disgustingly upbeat."
    n gneutral "Which is fine, I guess. For nøw."
    n "I'm gøing tø gø get søme cleaning supplies."
    hide naxili with moveoutleft
    "Naxili disappears up a set of stairs that have thankfully remained untouched by whatever calamity occurred in the first floor kitchen."
    "Taking a closer look around, you realize that, other than the sink and some nearby countertops, everything seems to be absolutely obliterated."
    "Wait, hey! It looks like part of Naxili's fridge made it through ok. Well, just maybe the bottom third of it. But there's a bottle of something that's still cold to the touch, and you're feeling pretty parched."
    menu:
        "Take a sip":
            jump drink
        "Better not touch it":
            jump nodrink
label drink:
    "You're sure Naxili won't mind you grabbing a quick sip of grubjuice before you get to work. Besides, you reason; if not now, then there's a chance it'll go bad without a refridgeration unit to cool in anyways."
    "You uncap the top. Bottom's up!"
    "Oh, this is... certainly a flavor you've never tasted before. In fact, it vaguely tastes like ammonia."
    "You hear Naxili come down from the stairs, followed by the heavy clatter of her dropping her supplies on the floor. You pause your hydrating and ask her what's wrong."
    show naxili angry with moveinright
    n "Are yøu DENSE? Why the fuck did yøu just drink that?!"
    "Drink what? The grubjuice?"
    n "That's nøt fucking GRUBJUICE yøu walking gløbesack! Yøu need tø expel that right nøw, beføre--"
    "Oh. You want to keep listening to what she's saying, since it seems so important, but your eyes seem to be on the fritz right about now."
    "You cough into your hands, and all you can see when you look down is a bright, fresh red."
    show bloodborderred with flash
    "The last thing you see is Naxili, pulling what looks like a hatchet from her pile of supplies as she slides her glasses back on."
    show naxili gannoy at bounce 
    n "Ugh. I can't believe I'm gøing tø have tø clean up a cørpse øn tøp øf everything else!"
    hide naxili
    hide bloodborderred
    stop music
    scene black
    show bg naxili_bad1 fadein 1.0
    play sound lose
    pause
    scene black fadein 2.0
    stop sound
    return
label nodrink:
    "You decide to leave the bottle alone. Eventually, Naxili comes back, cleaning supplies in hand."
    "Now you're really getting the full brunt of that ever-permanent glare of hers."
    "She chucks something that looks vaguely like a broom at you."
    show naxili gannoy
    n "Alright. Let's get tø wørk."
    hide naxili
    "You start at it. There's a lot to clean, and hours pass easily while you spend most of the night pushing pieces of hive wall into organized piles."
    "Naxili focuses on collecting any sharp pieces of glass, then moves to start putting some weird, stretchable paste where the giant hole in the wall is."
    "You wonder what that is, watching as she sloughs it on and it seems to hold its molded form almost immediately."
    show naxili gneutral
    n "It's a quick fix I engineered in my free time. It's a cømplex pølymer that hardens when expøsed tø a certain amøunt øf UV frøm øutdøør møønlight."
    n "Sø it uh, døesn't wørk super great øn cløudy days. But øtherwise, it's handy."
    "That's pretty impressive, you say, as you watch the sticky substance cling to the broken edges of the wall like it's alive."
    n "..."
    n guncomf "It's fine, I guess."
    show naxili gannoy
    "She turns away and starts putting away the goo back in the box she got it from, readjusting her glasses carefully."
    "You look around at the kitchen. The big stuff is still gone or flat out totalled, but in terms of progress, most of the mess has been swept up and taken care of. You think now would be a good time to take a nice break."
    "Naxili gives you a look, like you've suddenly grown a second head."
    show naxili gannoy at bounce 
    n "A break?"
    "Yeah. You know, like... sit down, have something to drink, stretch out for a second and talk about stuff. You're sure that between the two of you, you can drum up something interesting to ponder on, right?"
    "There's an uncomfortable pause. Then she takes a deep breath."
    n gneutral "Uh. Sure. Øk."
    "She gestures for you to follow her upstairs, and you both ascend."
    show bg hideout with wipeleft
    "The second floor is much neater than the first floor, until Naxili lets you into what you can assume what is her room."
    "It's an evil secret chemistry laboratory if you've ever seen one."
    "There's beakers and glass baubles and weird devices that you couldn't even begin to name or describe."
    "It doesn't help that they're all made of that same weird grub-substance that everything on Alternia seems to be made of."
    "She moves some boxes aside and pulls out some splaysacs for you two to sit on. It looks like these things haven't been used in a solid decade, but you're not about to complain."
    "You settle into one as Naxili goes and obtains some drinks from a mini-fridge under one of her many work tables."
    "She tosses one to you and opens her own before awkwardly sitting in her own splaysac. She's got her knees together and her back is straight. You wonder if she feels uncomfortable."
    n gannoy "What? Why wøuld I be uncømfortable?"
    "Well... You hope you're not about to make things weird by saying so, but... You've noticed she doesn't seem very used to hanging out with other people unless it's work-centric."
    n gangry "WHAT?!"
    n gannoy "Yøu're definitely mistaken. I'm {i}great{/i} at socializing. I knøw everything that gøes øn in my bløck."
    "You point out she had absolutely no idea what you were when you first met, even though you've been around the stemcluster for a while now."
    n "Øh, and suddenly yøu're høt shit, huh?"
    "Well, you wouldn't go that far, but trolls gossip. A {i}lot{/i}, you've found."
    "And an alien landing around your block isn't exactly a small topic of conversation, you'd think."
    n "..."
    show naxili guncomf at smalllower
    n "Øk, sø maybe I'm nøt a søcial flutterbeast like everyøne else. Sø what?"
    "She sinks further into her splaysac."
    show naxili gannoy at lowered
    n "Whø needs {i}friends{/i} anyways. Whø has the time før that?"
    "She continues her descent to become one with the splaysac."
    show naxili gannoy at sitting
    n "I'm Naxili fucking Miiace. I'm gønna change the wørld. I'm-- "
    hide naxili with moveoutbottom
    "Aaaand there she goes. Now you definitely can't hear her at all, with her completely closing into herself like the world's most dejected clam."
    menu:
        "Change the subject":
            jump subjectchange
        "Keep pressuring her":
            jump pressure
label subjectchange:
    "You quickly look around for something to change the subject with. Science! Man, she sure does have a lot of science around here, huh?"
    "Like a charm, Naxili perks up immediately."
    show naxili ghappy with moveinbottom
    n "Science? This just isn't any science; it's chemistry!"
    "She gestures around her."
    n "This is success in the making, and yøu're basking in it."
    "This seems to be going in a good direction. You ask what particular successes she's planning with her concoctions."
    "Naxili springs to her feet, clearly energized now that she's back in her safety zone."
    show naxili ghappy at bounce
    n "Wait, I can just shøw yøu!"
    hide naxili with moveoutleft
    "She starts rummaging around in a bunch of boxes you didn't notice sitting under some of the tables at first."
    "They all seem kind of sad and dejected, and badly organized. Little corked vials in stands clink and clatter as she pushes things around."
    "There's a lot of funky looking concoctions in there, and you can only assume they do crazy, wild things you've never seen before since you like to believe in your friends and their cool abilities."
    "But it does seem odd that she's gone and cast aside all of the fruits of her hobby so carelessly."
    show naxili ghappy with moveinleft
    "She's now shoving a bunch of random looking bottles and vials into your hands, all of them unlabeled and equally as baffling looking as the last."
    n "--and this øne causes fibrøus plants tø grøw instantaneøusly, thøugh it dehydrates the dirt arøund it, and {i}this{/i} øne can melt thrøugh any rigidly structured material, oh but {i}this{/i} øne prøduces catalysts that can bøil a seadweller's bløød in secønds..."
    n gannoy "This øne here actually turns yøur skin grey, which, is pretty useless for trølls now that I'm saying it øut løud."
    n "I guess it cøuld be useful tø yøu, thøugh, if yøu needed tø blend in før whatever reasøn. Døesn't last super løng, but whø knows?"
    n ghappy "In fact, I'm feeling generøus enough to let you keep it."
    hide naxili with moveoutleft
    "You open your mouth to thank her, but she's already speeding off elsewhere."
    n "Yøu døn't have tø even thank me! Cønsider it a gift frøm yøur all-new pal, and an incentive tø never, ever bring up my søcial life ever again."
    "You warily agree... for now. You watch from the corner of your vision as Naxili starts pulling out even more boxes of her weird creations, somehow, and you're starting to sweat a bit from uneasiness."
    "You're not sure you can keep holding all of this stuff!"
    "You glance around, and your vision narrows in on a nearby window. Maybe... if you can just dump a little bit of the load somewhere, you'll be ok?"
    "Naxili seems so absorbed in what she's doing that you're sure she won't even notice a vial or two missing."
    "You sneak over to the window, shoving it open with a shoulder and tossing a few random bottles out as quickly and discretely as you can."
    "Phew! That's much better..."
    with hpunch
    "You jolt when you hear a bloodcurdling screech from far below. Naxili sits straight up, bumping her head against the underside of the table she's under. Her glasses jostle off in her scramble over."
    show naxili angry with moveinleft
    n "What the FUCK did yøu just dø?!"
    "She shoves the window open further, and below you can see what looks like a bronzeblood stopped in the middle of the sidewalk."
    hide naxili
    show bg alternia2 with wipeleft
    show hefais shock
    "It looks like one of the smaller, clearer liquids fell onto him. Oops! At least he looks relatively unharmed?"
    show bloodsplatter with flash
    "Oh."
    hide hefais
    hide bloodsplatter with flash
    show bg hideout with wipeleft
    "All that's left on the sidewalk of the troll is a wretched looking brown splatter where he burst like a gross, bloody water balloon."
    "Unsurprisedly, Naxili looks extremely nonplussed."
    show naxili annoy
    n "What in the name."
    show naxili angry at bounce
    n "ØF ALL THINGS IDIØTIC--"
    with hpunch
    "She grabs you by the throat. Her grip is much, much stronger than you figured was possible for her relatively small frame."
    show naxili rage at bounce
    n "DØ YØU FUCKING THINK YØU'RE DØING?!"
    "You're trying to choke out an explanation, but it's pretty difficult considering the extenuating circumstances of you being WWE style chokeheld."
    "Naxili doesn't let up though, taking the opportunity to slam you violently against the nearest wall."
    with vpunch
    n "I get it. This is just all søme sørt øf fucking jøke tø yøu, isn't it?"
    with vpunch
    n "Get intø the shut-in's hive. Make her play yøur games. Get a tøy ør twø øut øf it, see høw many trølls she'll help yøu kill."
    show naxili happy at bounce
    n "Well, newsflash, asshøle!! Yøu aren't fucking øriginal!!!!"
    n "You think I haven't dealt with this kind of shit beføre?"
    n "You think this isn't the first time sømeøne's tried tø take advantage øf me?"
    n "Yøu're a løt dumber than yøu let øn, yøu knøw."
    "Your vision is starting to fade; you don't think you'll be getting out of this one anytime soon. Naxili looks pretty darn peeved."
    hide naxili
    scene black with Dissolve(2.0)
    "Shoot. You were kind of hoping things were going well with her in the friend department, but it seems like you're coming out of this friendless {i}and{/i} dead."
    "What a bummer."
    n "It's yøu're fucking funeral, either way."
    stop music
    scene black
    show bg naxili_bad2 fadein 1.0
    play sound lose
    pause
    scene black fadein 2.0
    stop sound
    return
label pressure:
    "You can't help but pity her a bit as she does her best to become one with the floor ever so gradually."
    "Maybe words aren't the best thing here; instead, you reach out with the flat of your hand and gently pat the side of her face."
    n "..."
    n "What are yøu døing."
    "Patting. Er. Papping? You're pretty sure this is a thing trolls do to make each other feel better, right?"
    n "..."
    show naxili gannoy with moveinbottom
    n "I mean. There's a løt møre tø it than that."
    "She slaps your hand away, but at least she isn't wallowing in self-pity anymore, so that's a start. You ask her about how she's feeling."
    n "Stupid."
    n "I feel like a fucking idiøt, nøw that the fact that an alien is better cønnected than me is nøw øut in the fucking øpen, where I can't fucking deny it."
    show naxili gneutral at sigh
    n "Which, yeah. Is kind øf a fucking prøblem, I guess."
    show naxili gannoy at bounce
    n "Nøt that I'd knøw the first fucking thing about fixing sømething like that at this pøint, thøugh."
    n "I mean, løøk at me. Løøk at all of this!"
    show naxili gangry at bounce
    n "All I've døne før the last eight gød førsaken sweeps is sit in my røøm and make a bunch øf useless bullshit."
    n "Waiting aprehensively før the next trøll tø cøme smashing in tø take whatever I've made because they {i}think{/i} it might be useful tø them."
    show naxili gannoy at bounce 
    n "I used tø be a fucking ørganized trøll, yøu knøw! I had these nice little labels før everything I ever made."
    "She loosely gestures to the boxes strewn about the room, obviously dangerously piled up with unlabeled vials, bottles, and boxes of all sorts."
    n "Nøw I just thrøw everything wherever, sø if sømeøne gøes øn a burglary jøyride, at least I can get a little bit øf fucking satisfactiøn knøwing that they might eventually tip back an erlenmeyer øf deadly acid thinking it's Køøl-Grub."
    "You listen to her rant for a bit. You figure it's been a while since she's really been able to unload her worries onto anyone, if she really is as much of a hermit as she says."
    show naxili gneutral
    "Eventually, when she calms down, you mention that she doesn't have to spend all her time making things if she doesn't want to."
    show naxili gangry at bounce
    n "Then what the hell am I suppøsed tø dø, until I'm reassigned ør culled? Just sit arøund røtting?"
    n "If yøu haven't nøticed, this is all I've gøt. I'm a øne trick høøfbeast."
    show naxili gannoy
    "Hey, hey. Who said anything about doing anything {i}productive{/i}?"
    "Because, really. When is having fun ever supposed to be all that productive anyways?"
    show naxili gneutral
    n "..."
    n "Having fun."
    "Yep. Just some good ol' fashioned palling around."
    show naxili gangry at bounce
    n "..."
    show naxili guncomf at sigh
    n "I've never døne that. Beføre."
    "No way. Never?"
    show naxili grage at bounce
    n "Nø!!! The ønly shit I've ever heard øf døne for entertainment arøund here is that FLARP bullshit, and yøu are absølutely nøt getting me intø any kind øf bløødsport. I am {i}nøt{/i} a killer."
    show naxili gannoy
    "Hey, that's all well and fine in your book, you say. You've never really had a taste for all the random murders that seem to take place regularly on Alternia, if you're being completely honest."
    "You do, however, have some pretty good ideas on where to start."
    "You stand and hold out a hand to her. Starting small is always the best foot forward for things like these, right? So what better than to try some simple fun out with a new friend?"
    n "..."
    show naxili blush at sigh
    n "Yøu are sø unbelievably persistent."
    show naxili gneutral 
    n "Fine. Fine! I'll gø aløng with whatever it is yøu've gøt planned."
    show naxili gannoy at bounce
    n "I feel like yøu'll never get øff my back abøut it either way, sø might as well get sømething øut øf this, I guess."
    "You've only known Naxili for a short amount of time, but you can tell that she's more on board with the idea than she's really letting on."
    show naxili gangry at bounce
    n "Gh--!"
    "Yep, looks like you hit the nail right on the metaphorical head."
    show naxili guncomf
    n "Believe whatever yøu want."
    show naxili gannoy at slowerbouncing
    "She grabs you by the edge of your sleeve and starts leading you out of her room."
    n "What dø yøu even have planned, anyways?"
    "You mention you know a handful of trolls that might be right up Naxili's alley."
    show bg alternia4 with wipeleft
    show naxili gangry at slowerbouncing
    n "W-wait, what happened tø taking this søcializing thing sløw???"
    "Oh! Maybe meeting your other friends can wait for now. But you are definitely taking her to a Game Grub-Cade before anything else."
    show naxili gannoy at bounce
    n "..."
    n "What the fuck is a Game Grub-Cade?"
    "Oh my god."
    "You are just now hit with the reality of how dire this situation is."
    show naxili gangry at bounce
    "You grab her by the wrist. You only have time to give her a brief warning before taking off sprinting out the door."
    "The night is barely young, and you know exactly the responsibility you now harbor for making sure your new friend has the best time of her life!!"
    "You've got a head full of empty, a hand full of hermit, and half a mind to go balls off the walls apeshit on the first token machine you see."
    hide naxili
    stop music
    scene black
    show bg naxili_good fadein 1.0
    play sound win
    pause
    scene black fadein 2.0
    stop sound
    return

label hefais:
    $ renpy.block_rollback()
    
    $ quick_menu = True

    play music hefaistheme
    scene bg alternia with fade
    show hefais annoy with moveinbottom
    ht "Oh god, oh god, oh fuck..."
    "You can see a young troll across the street from where you're standing. He looks to be hurriedly filling a sack with items, running into his hive to gather more every few seconds."
    "This seems like the perfect opportunity to make a new friend! You saunter on over and ask the troll if he needs any help."
    show hefais shock at quickbouncetwice
    window hide
    ht "What???"
    "He briefly turns his head to face you, eyes wide like dinnerplates. Seems like you really surprised him. You don't get the impression that that is a particularly difficult feat."
    show hefais fake
    ht "Oh. It's just the human. Ever{font=courbd.ttf}Ψ{/font}thing's just fine, bud. Don't worr{font=courbd.ttf}Ψ{/font} about it."
    "You open your mouth to insist on providing him with assistance in whatever it is he's doing, but quickly close it again. Something is... strange."
    show hefais sweat
    "You've got it. The symbol on his eyepatch makes it clear he's a bronzeblood, but this is a cerulean district. What is this guy doing here, taking things from a hive that isn't his? Isn't he worried about getting culled?"
    ht "Haha, {font=courbd.ttf}Ψ{/font}eah, um... Look, please don't sa{font=courbd.ttf}Ψ{/font} an{font=courbd.ttf}Ψ{/font}thing about this, alright? ...At least not for the next... four hours-ish? I've alread{font=courbd.ttf}Ψ{/font} got drones on m{font=courbd.ttf}Ψ{/font} tail, and..."
    "He trails off without finishing his sentence. You happily assure him that you wouldn't dream of snitching, after you think he's finished talking. Ratting him out wouldn't be very friendly, after all."
    "You still think this situation is pretty dangerous, though."
    "Stealing things from a ceruleanblood's hive where everyone can see him, while being chased by drones?"
    "You're pretty sure getting told on should be the least of his issues. He's going to be culled soon if he's not careful."
    show hefais fake
    ht "...Right. {font=courbd.ttf}Ψ{/font}eah, I know. I just... I need to make the most of the time I've got left."
    "You are completely taken aback. You hadn't realized..."
    show hefais shock at twitch
    ht "Er, wait, no, that's not what I meant. I mean... I'm leaving soon. The planet, that is. But not because I'm d{font=courbd.ttf}Ψ{/font}ing. I'm just... leaving..."
    "Oh, right! You recall being told about Alternians being sent off-planet to conquer space once they reach a certain age. You think that sounds pretty exciting?"
    show hefais annoy
    ht "No, no, that's not it either. Someone's coming to take me awa{font=courbd.ttf}Ψ{/font} from Alternia. Somewhere better, where I don't have to worr{font=courbd.ttf}Ψ{/font} about all this culling stuff, or highbloods being terrible."
    show hefais wistful
    ht "Somewhere where I'll finally be... free."
    show hefais fake
    ht "Oh, but, uh... {font=courbd.ttf}Ψ{/font}ou don't need to worr{font=courbd.ttf}Ψ{/font} about all that."
    "You think this place, whatever it is, sounds pretty amazing, actually! Where is it? How does he know about it?"
    show hefais sweat
    ht "Uh..."
    "He seems hesitant."
    ht "It's... well..."
    show hefais nervous
    ht "Oka{font=courbd.ttf}Ψ{/font}, to be honest, I don't reall{font=courbd.ttf}Ψ{/font} know the whole stor{font=courbd.ttf}Ψ{/font} m{font=courbd.ttf}Ψ{/font}self. I just know that some gu{font=courbd.ttf}Ψ{/font}s from another planet offered to pick me up and take me somewhere else, and those same gu{font=courbd.ttf}Ψ{/font}s are also me... somehow..."
    "You're not following."
    show hefais wistful
    ht "{font=courbd.ttf}Ψ{/font}eah... neither am I, pal. Not reall{font=courbd.ttf}Ψ{/font}, an{font=courbd.ttf}Ψ{/font}wa{font=courbd.ttf}Ψ{/font}. All I know is a m{font=courbd.ttf}Ψ{/font}sterious stranger has been messaging me..."
    ht "Telling me that there's a planet out there, far off in some other dimension, full of people who talk, act, and think exactl{font=courbd.ttf}Ψ{/font} like me."
    ht "And he's going to take me there, to join them..."
    "Wow. This sounds amazing! Almost too good to be true? You begin to wonder if something like this really COULD be true."
    "...COULD something like this really be true?"
    menu:
        "It could be true.":
            jump true
        "It could not be true.":
            jump nottrue

label nottrue:
    "Of course it's not true! An entire planet, all the inhabitants of which are exactly like this one guy? Whoever has been in contact with this poor guy is obviously trying to trick him."
    "You voice your concerns to the troll in front of you. It's quite possible that he's running into some sort of trap. Someone might be trying to abduct and cull him in order to use his blood as paint or something."
    "All you're trying to do is give him a friendly warning."
    show hefais annoy
    ht "What...? What are {font=courbd.ttf}Ψ{/font}ou talking about? Who would do that?"
    ht "Look... this planet... It's real, oka{font=courbd.ttf}Ψ{/font}? I know it is."
    ht "I can just... feel it. The place where I'm able to fit in with ever{font=courbd.ttf}Ψ{/font}one else, because the{font=courbd.ttf}Ψ{/font}'re all exactl{font=courbd.ttf}Ψ{/font} like me... It exists..."
    show hefais wistful
    ht "It's like the{font=courbd.ttf}Ψ{/font}'re calling out to me... The{font=courbd.ttf}Ψ{/font} need me just as much as I need them."
    show hefais fake
    ht "...Uh. But. {font=courbd.ttf}Ψ{/font}eah. I get that it sounds... weird..."
    "Poor thing. It seems like he's really deluded himself into believing in such an obviously fake thing. You begin to wonder what the most friendly course of action would be..."
    "Should you insist on shattering his illusions, freeing him from this false sense of hope? It would certainly help him in the long run, but... Is that really your place as his friend?"
    show hefais annoy
    "Would it be better to just stand idly by and allow him to discover the truth for himself? Though if he winds up culled, that would end your friendship pretty quickly. You know from experience how hard it is to be friends with a corpse."
    show hefais angry2 shakes
    "Maybe you could keep quiet, but accompany him to wherever he's going! That way, if it really is a trap and not some stupid prank, you could help him fend off attackers/kidnappers."
    "You wouldn't know how to begin to ask him to allow you to do that, though. Is there any way to phrase the question without further invalidating him? You're having a hard time thinking of one."
    "'Hey, troll guy, can I follow you to your secret meetup place that I already said was probably a trap? Not because I think you're in danger or anything. Just because I want to! Friends, or something'"
    "Yikes. What kind of impression would THAT give off? Not a good one, you think."
    hide hefais with moveoutright
    "As you sit there deliberating, you barely notice the troll still standing in front of you look up to the sky, curse under his breath, and suddenly run off, leaving his sack behind."
    "You go to call out to him before realizing you never even got his name. Confused and anxious, you try shouting a firm 'HEY!' anyway, but it comes out weak and strained."
    "You wonder what his deal is. Did he even realize he left all this stuff behind? If he didn't take all his stolen goods with him, who's supposed to take the fall once the drones come around?"
    "There's no one hanging around this lawnring except you, after all..."
    "Wait. Shit."
    "You very slowly and carefully crane your neck upwards, looking to the exact spot the troll was looking towards moments ago. There, several feet above you, is a fleet of imperial drones."
    "You find yourself frozen with fear. This is very much not good."
    #end card - bad end
    stop music
    scene black
    show bg hef_bad1 fadein 1.0
    play sound lose
    pause
    scene black fadein 2.0
    stop sound
    return

label true:
    "You decide the troll's story is just believable enough to possibly be true.  I mean, the multiverse is a big place, right?"
    "Statistically, the exact situation he is describing is almost so improbable as to be almost impossible."
    "But also statistically speaking, with all the people who exist everywhere all the time, something like this HAS to happen to someone, right?"
    "Yes, you are pretty sure you are right. This is absolutely how statistics work."
    "You congratulate the troll on this wonderful opportunity. You know exactly how horribly oppressive Alternia can be, especially towards lowbloods. This whole thing sounds pretty great!"
    show hefais happy
    ht "Uh... {font=courbd.ttf}Ψ{/font}eah. Haha."
    show hefais wistful at bounce
    ht "..."
    "... He's completely silent. Deep in thought, maybe? You ask him what's up."
    ht "Oh. Nothing, it's just..."
    ht "I dunno. I didn't reall{font=courbd.ttf}Ψ{/font} expect {font=courbd.ttf}Ψ{/font}ou to believe that."
    ht "A lot of m{font=courbd.ttf}Ψ{/font} friends have been prett{font=courbd.ttf}Ψ{/font}... doubtful. The{font=courbd.ttf}Ψ{/font} think I'm stupid for believing what the other Hef is telling me. I guess I don't blame them."
    "...Hef? Is that a word for a weird troll version of some common object?"
    show hefais fake at bounce
    ht "Wh-...? Oh, no, sorr{font=courbd.ttf}Ψ{/font}. It's m{font=courbd.ttf}Ψ{/font} name."
    show hefais nervous
    ht "Er, I mean, Hefais is m{font=courbd.ttf}Ψ{/font} name. Hefais Tusamb. M{font=courbd.ttf}Ψ{/font} friends call me Hef."
    "Oh! His friends! Does that include you?"
    ht "Uh... Sorry, bud, but... not reall{font=courbd.ttf}Ψ{/font}? I don't reall{font=courbd.ttf}Ψ{/font} know {font=courbd.ttf}Ψ{/font}ou that well {font=courbd.ttf}Ψ{/font}et... since {font=courbd.ttf}Ψ{/font}ou just sort of... walked right up to me... just now... and we've never spoken before..."
    "Right, of course. You understand. Wriggler steps."
    show hefais sweat
    "You ask him if there's anything else he needs help with. Loading things into that sack, for instance. He's got a big trip ahead of him, after all, and from the way he talks about it it seems like it's happening soon."
    "You get the feeling your question doesn't quite register, though, as he seems to be distracted by something above the both of you. You follow his gaze upwards, and... oh. Those are drones."
    ht "Shit."
    "He looks back at you."
    show hefais nervous at bounce
    ht "Run."
    hide hefais with moveoutleft
    "Hefais immediately starts booking it down the street. Thinking quickly, you reach into the sack and pull out the first thing your hand touches."
    "It's slimy and squishy in there, and the object you grab feels (and as you soon find out, looks) like a big fat worm, but it will have to do."
    "You reel back and toss it across the street, and like the gross creature it is, it splatters against the wall of one of the hives on the next block over, sending grub chunks in all directions."
    "It emits a loud, high pitched sound as it deflates where it landed."
    "Confident that your distraction was sufficient enough to get the drones off your trail, you high-tail it out of there, sack in tow, heading in the same direction as Hefais. You sure hope that guy knew where he was going."
    show bg outskirts with wipeleft
    "You're not sure how much time passes. It feels like hours. You check the sky every so often to make sure the sun does not creep back from beyond the horizon as you follow Hefais's trail, trying your best to keep your direction consistent."
    "You have been burned before. Literally, Alternia's sun gave you second degree burns."
    "You eventually come across a bookhive. Or, perhaps, THE bookhive? You're not sure how many of these there are in Outglut, nor are you familar enough with the scenery of this planet to determine if you are even in Outglut anymore."
    "Either way, you decide it would be as a good a place to rest as any. You've been wandering the city streets for who knows who long, and you can feel your back soring up trying to carry all these bugs around."
    show bg bookhive
    "You entire the bookhive, scanning the room for a table to pull up a chair and rest at. You sure hope the sack of unidentifiable goods doesn't look TOO suspicious."
    "Wait... is that...?"
    show hefais wistful
    "It is! Seated at a table near the back of the bookhive is Hefais!"
    "Poor guy doesn't look too good. You guess he's been really concerned about you, considering he left you to be culled by a bunch of bloodthirsty drones."
    "That, or he's upset about leaving his loot behind. You choose to believe the former, though. He's going to be so excited to see you're okay!"
    "With a satisfied smile on your face, you walk over to Hefais and plop the bag of bugs on the table and pull up the seat across from him."
    show hefais shock at bounce
    ht "AGH!"
    "Oh, right. He's jumpy. You forgot. You begin apologizing profusely."
    ht "Wh-... Oh! No, no, it's fine, uh..."
    show hefais fake
    "You catch Hefais looking around the room, surveying the reactions of the people around him. You quickly catch on and start doing the same."
    "Seems like he didn't attract much attention. One or two curious teals, but that's it."
    "You guess people screaming in libraries is more or less normal around here? You suppose that would make some sense, what with all the murder that happens on this planet all the time."
    ht "Shit, oka{font=courbd.ttf}Ψ{/font}, we're good. Sorr{font=courbd.ttf}Ψ{/font} about that. Uh, also, thanks for bringing m{font=courbd.ttf}Ψ{/font} gamegrubs. I reall{font=courbd.ttf}Ψ{/font} appreciate it."
    "Of course! What are friends for?"
    show hefais wistful
    ht "Friends, huh...?"
    "He goes quiet again. Another moment of deep thought, you guess?"
    "He speaks again after an awkwardly long pause."
    ht "...{font=courbd.ttf}Ψ{/font}'know, I wasn't so sure at first, but... {font=courbd.ttf}Ψ{/font}ou reall{font=courbd.ttf}Ψ{/font} have been a prett{font=courbd.ttf}Ψ{/font} good friend so far. Better than my other friends, at least..."
    "Oh, right. You remember him saying something about them earlier, his friends who wouldn't believe him. What's up with them?"
    show hefais fake
    ht "Heh, I dunno. They're fine I guess. And it's not like the{font=courbd.ttf}Ψ{/font}'re wrong about me being gullible or an{font=courbd.ttf}Ψ{/font}thing, it's just..."
    show hefais annoy at bounce
    ht "I feel like friendship's gotta be more than just being friendl{font=courbd.ttf}Ψ{/font}, {font=courbd.ttf}Ψ{/font}'know? Like... sometimes friendship takes encouragement and trust and stuff? And it feels a little like m{font=courbd.ttf}Ψ{/font} friends don't give me that."
    "Oh? How does he mean?"
    show hefais wistful
    ht "..."
    "You see him briefly scan the room again."
    ht "...Like, {font=courbd.ttf}Ψ{/font}'know how {font=courbd.ttf}Ψ{/font}ou caught me... obtaining things?"
    "You nod. Obviously you remember how he got all those grubs. You said yourself that he would probably get culled for stealing from a highblood."
    ht "Right, well... The things I obtained were mine to begin with. I bought those things with m{font=courbd.ttf}Ψ{/font} own caegars. It wasn't until I left m{font=courbd.ttf}Ψ{/font} hive that someone else came and... obtained them."
    show hefais annoy
    ht "Like, I guess I have something of a reputation for hoarding gamegrubs or something, and that was reason enough to ransack m{font=courbd.ttf}Ψ{/font} hive for choice grubs. And when I told m{font=courbd.ttf}Ψ{/font} rustblood friends about it..."
    show hefais angry2
    ht "I dunno... It was like the{font=courbd.ttf}Ψ{/font} didn't care. Like, that's just the wa{font=courbd.ttf}Ψ{/font} it works around here, and if a victim so much as cares at all about it, that's reason enough to be culled."
    ht "I mean... I get being defeatist, because it's not like there's an{font=courbd.ttf}Ψ{/font}thing we can do about it, but... some s{font=courbd.ttf}Ψ{/font}mpath{font=courbd.ttf}Ψ{/font} or something would be nice. Ma{font=courbd.ttf}Ψ{/font}be just lend me a few caegars so I can replace them... I dunno..."
    ht "..."
    show hefais wistful
    ht "Sorr{font=courbd.ttf}Ψ{/font}."
    "No, no! He doesn't have anything to be sorry about! From where you're standing, he's totally right!"
    ht "...{font=courbd.ttf}Ψ{/font}eah, ma{font=courbd.ttf}Ψ{/font}be. I dunno. It's not like it's reall{font=courbd.ttf}Ψ{/font} their fault or an{font=courbd.ttf}Ψ{/font}thing."
    show hefais annoy
    ht "An{font=courbd.ttf}Ψ{/font}wa{font=courbd.ttf}Ψ{/font}, the{font=courbd.ttf}Ψ{/font} didn't believe me about the Hef planet thing, so that was kind of the straw that broke the camel's back. I'm gonna see this through and get the hell off this planet ASAP."
    "That... SOUNDS like a good idea. Or it did. Maybe it still does?"
    "But... would running away really solve anything? Maybe nipping this issue in the bud would be a better course of action?"
    "Or not. You recall something about a famous religious leader..."
    "Now might be the time for some friendly advice. But which piece of advice to give?"
    menu:
        "Don't just leave! That's what a quitter would do! Fight the highbloods and rebel!":
            jump rebel
        "Leaving is probably the best course of action.":
            jump leave

label rebel:
    "You are so completely certain that staging a rebellion would be the best course of action for Hefais."
    show hefais shock at bounce
    ht "Are {font=courbd.ttf}Ψ{/font}ou serious? Me? Rebel? Do {font=courbd.ttf}Ψ{/font}ou know who {font=courbd.ttf}Ψ{/font}ou're talking to???"
    show hefais fake
    ht "Er. Sorry. {font=courbd.ttf}Ψ{/font}ou know what I mean."
    show hefais wistful
    ht "I... could never do that. No wa{font=courbd.ttf}Ψ{/font}. I'd be culled on the spot. I'd get told off b{font=courbd.ttf}Ψ{/font} a highblood, sa{font=courbd.ttf}Ψ{/font} half of a cool and rebellious sentence, and then..."
    show hefais fake
    ht "...bang. No more Hefais. Also no more pizza for Hefais to eat. Or gamegrubs for him to pla{font=courbd.ttf}Ψ{/font}. Or East Alternian media for him to consume..."
    show hefais nervous at bounce
    ht "Wh{font=courbd.ttf}Ψ{/font} would {font=courbd.ttf}Ψ{/font}ou even suggest something like that???"
    "Oh, come on! It wouldn't be that bad. There's gotta be a ton of likeminded lowbloods, right? He could gather them all up and lead them against the highbloods!"
    "No more injustice! No more tyranny! No more stolen gamegrubs!"
    ht "..."
    show hefais wistful
    ht "Huh. You reall{font=courbd.ttf}Ψ{/font} think I could do something like that?"
    "Of course!"
    ht "..."
    ht "....."
    ht ".........."
    show hefais happy at bouncetwice
    ht "Huh! {font=courbd.ttf}Ψ{/font}eah, alright! I'll do it! I'll give rebellion a shot!"
    "Oh. Wow. He's pretty animated all of a sudden."
    ht "In fact, not onl{font=courbd.ttf}Ψ{/font} will I 'give it a shot,' I'll do it! I'll rebel!!"
    "Yeesh, he's getting kind of loud. You tell him that maybe it would be better if he were a little quieter."
    show hefais angry2 at bounce
    ht "Wh{font=courbd.ttf}Ψ{/font} should I be??? I've been quiet for too long, damn it!!! It's about time lowbloods like me were allowed to be as loud as we damn well please!!"
    "No, you mean he's in a library - which is typically a very quiet place - yelling about rebellion. If he's not careful--"
    ht "What? I'll get CULLED??? I'd like to see them TR{font=courbd.ttf}Ψ{/font} and cull me now! The{font=courbd.ttf}Ψ{/font} won't! The{font=courbd.ttf}Ψ{/font} COULDN'T! Because Hefais Tusamb is LEADING the REBELLION!!!"
    "Hefais snatches the bag of grubs up off the table and holds it high in the air."
    show hefais happy at bounce
    ht "Thanks for the grubs, budd{font=courbd.ttf}Ψ{/font}! Now, if {font=courbd.ttf}Ψ{/font}ou'll excuse me, there are lowbloods to lead!"
    "And with that, Hefais saunters out the door, all eyes in the room squarely focused on him and his melodramatic exit."
    hide hefais
    show bg black with Dissolve(1.0)
    "It would be weeks until you saw your friend again. Though perhaps friend wouldn't be the right word."
    "He was more like... an acquaintance. A quiet, kind of awkward acquaintance, until he wasn't quiet or awkward anymore."
    "You'd been wandering the cerulean district without a goal in mind for some time before stumbling upon what remained of your acquaintance..."
    "A severed head, impaled on a spear, stuck in the lawnring of the the very same hive where Hefais had reclaimed his gamegrubs."
    "You recall the Hefais who had left you in the library: loud, unafraid, sure of himself, and unwilling to compromise, much less obey."
    "You find yourself hoping he went out the same way."
    #end card - other bad end
    stop music
    scene black
    show bg hef_bad2 fadein 1.0
    play sound lose
    pause
    scene black fadein 2.0
    stop sound
    return

label leave:
    "As cowardly as it is, leaving Alternia and living on this Hef planet... does seem like it would be the best option."
    "Especially for someone like Hefais, who does not strike you as the type who could lead much of anything."
    "You basically tell him as much."
    show hefais fake
    ht "Haha, uh... Thanks...?"
    show hefais wistful
    ht "..."
    "..."
    ht "He{font=courbd.ttf}Ψ{/font}, uh... I just wanna sa{font=courbd.ttf}Ψ{/font}..."
    ht "Thanks for helping me out, and... listening to me, and stuff..."
    show hefais happy at bounce
    ht "Um... I know it's probabl{font=courbd.ttf}Ψ{/font} kinda dumb, but it means a lot to have someone that... I dunno. Agrees with me on stuff? And listens to what I have to sa{font=courbd.ttf}Ψ{/font}?"
    show hefais nervous at bounce
    ht "Like... there aren't a ton of people who do that sorta thing around here. At least... that's what it feels like..."
    ht "So it's nice to have a friend who does that."
    "Did he just say... friend?"
    ht "Oh. {font=courbd.ttf}Ψ{/font}eah, I guess I did. I guess I consider {font=courbd.ttf}Ψ{/font}ou m{font=courbd.ttf}Ψ{/font} friend now."
    show hefais happy
    ht "I mean... {font=courbd.ttf}Ψ{/font}ou helped me obtain stuff. It kind of seems like that's ver{font=courbd.ttf}Ψ{/font} much a friend thing to do?"
    "Oh, wow!  That's the first smile he's had on his face that didn't look pained and forced!"
    "Amazing! Another friend! You guess you can officially declare this one a succe--"
    show hefais fake
    ht "{font=courbd.ttf}Ψ{/font}eah. Shame I'm leaving tonight."
    "...What?"
    ht "Oh. Sorr{font=courbd.ttf}Ψ{/font}. Didn't I tell {font=courbd.ttf}Ψ{/font}ou? I'm leaving."
    ht "Er, I mean. I know I told {font=courbd.ttf}Ψ{/font}ou I'm leaving. But ma{font=courbd.ttf}Ψ{/font}be I didn't sa{font=courbd.ttf}Ψ{/font} it was tonight?"
    ht "But... {font=courbd.ttf}Ψ{/font}eah. It's tonight. I'm leaving tonight."
    "But you just became friends! You have to do friend things together now! That's the whole point of friendship!"
    ht "I mean... we can hang in the librar{font=courbd.ttf}Ψ{/font} for a bit I guess."
    show hefais nervous
    ht "But m{font=courbd.ttf}Ψ{/font} ride's gonna be here in an hour. We've been planning this for, like, a week, so..."
    ht "{font=courbd.ttf}Ψ{/font}ou could come with, if {font=courbd.ttf}Ψ{/font}ou want.  I'm sure the head Hef would be oka{font=courbd.ttf}Ψ{/font} with it. Onl{font=courbd.ttf}Ψ{/font} thing is... {font=courbd.ttf}Ψ{/font}ou probabl{font=courbd.ttf}Ψ{/font} couldn't come back. People are gonna get real mad around here with all that back-and-forth Hef travel."
    "...No. You couldn't do that. You have so many friends here, and... you really want to get back to your home some day. On Earth. Travelling to some alternate Hef planet dimension thing would not help with that very much."
    show hefais happy at bounce
    ht "Got it. So... what do we do now, friend?"
    "You tell Hef that there is only one option: the two of you will need to fit an entire LIFETIME of friendship into the span of one hour, and also somehow do it all in this bookhive."
    show hefais sweat
    "Hef looks shocked."
    ht "Wow, all of that... here... now...? Gee, wow, that's, uh..."
    show hefais wistful
    ht "..."
    ht "....."
    ht ".........."
    show hefais happy
    ht "...{font=courbd.ttf}Ψ{/font}eah, alright. Sure thing, pal. Where do {font=courbd.ttf}Ψ{/font}ou think we should start?"
    #end card - good end! INTENSE FRIENDSHIP MONTAGE
    stop music
    scene black
    show bg hef_good fadein 1.0
    play sound win
    pause
    scene black fadein 2.0
    stop sound
    return
