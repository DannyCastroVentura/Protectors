################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Transforms
################################################################################

# styles
transform farLeft:
    xalign 0
    yalign 1.0

transform midLeft:
    xalign 0.3
    yalign 1.0

transform farMidLeft:
    xalign 0.1
    yalign 1.0

transform midRight:
    xalign 0.7
    yalign 1.0

transform farMidRight:
    xalign 0.9
    yalign 1.0

transform farRight:
    xalign 1.0
    yalign 1.0

transform fit_to_screen_height:
    fit "contain"  # scales image to fill as much as possible without cutting or distorting 
    xalign 0.5   # Center horizontally
    yalign 0.5   # Center vertically if needed

transform stretch_fullscreen:
    xysize (config.screen_width, config.screen_height)

style hover_white:
    color "#b3b3b3"
    hover_color "#ffffff"
    
style hover_black:
    color "#b3b3b3"
    hover_color "#000000"

style red_hover_red_dark:
    color "#ff0000"
    hover_color "#880000"

transform notify_fade:
    alpha 0.0
    linear 0.5 alpha 1.0     # Fade in over 0.5 seconds
    pause 2.0                # Stay fully visible
    linear 0.5 alpha 0.0     # Fade out over 0.5 seconds

screen notify(message):
    frame:
        at notify_fade
        style "notify_frame"
        xalign 1.0
        yalign 0.1

        text message style "notify_text"

    timer 30.0 action Hide('notify')


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5   # Center horizontally
        yalign 0.5   # Center vertically
        spacing 20   # Space between menu choices
        for i in items:
            textbutton i.caption action i.action

screen custom_menu(items):
    style_prefix "choice"

    vbox:
        xalign 0.5   # Center horizontally
        yalign 0.8   # Center vertically
        spacing 20   # Space between menu choices
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900

style button_in_black_background:
    color "#9b9999"
    hover_color "#ffffff"
    padding (10, 5)
    xminimum 200                    # ensures consistent width
    yminimum 50

style option_button_online_shop:
    background "#555"   # normal dark gray
    hover_background "#fff"  # lighter gray when hovered
    padding (5, 5)
    xalign 0.5
    yalign 0.5

style rarity_navegation_text_online_shop:
    color "#555"
    hover_color "#fff"
    padding (10, 5)
    xalign 0.5

style rarity_navegation_text_online_shop_active:
    color "#fff"
    padding (10, 5)
    xalign 0.5

style text_boss_expedition_button:
    color "#ffffff"
    xalign 0.5
    yalign 0.5

style background_boss_expedition_button:
    background "#555"
    hover_background "#752121"
    padding (20, 10)
    xalign 0.5
    yalign 0.5

style background_expedition_button:
    background "#555"
    hover_background "#2E5530"
    padding (10, 5)
    xalign 0.5

style square_button:
    xminimum 200
    yminimum 200
    xmaximum 200
    ymaximum 200
    background "#a5a5a5"
    hover_background "#666"
    size 20

style rectangle_button:
    xminimum 200
    yminimum 75
    xmaximum 200
    ymaximum 75
    background "#a5a5a5"
    hover_background "#666"
    size 20

style message_boss_expedition_textbutton:
    color "#666"
    hover_color "#ffffff"
    xalign 0.5
    yalign 0.5

style message_boss_expedition_textbutton_your_turn:
    color "#666"
    xalign 0.5
    yalign 0.5

screen my_weapons_screen():
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 300
        $ buttons_background = im.Scale("images/background_item.png", scale, scale)

        # Close button - top right
        textbutton "Back" action Hide("my_weapons_screen"):
            text_style "hover_white"
            xalign 1.0
            yalign 0.0
            padding (10, 5)
        vbox:
            spacing 50
            xalign 0.5
            yalign 0.1
            null height 10
            text "Weapons" size 50 color "#FFF" xalign 0.5

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    spacing 20

                    frame:
                        xalign 0.0
                        yalign 0.0
                        padding (10, 10)
                        background Solid("#000000f1")
                        has vbox
                        
                        # Scrollable quest list
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True

                            vbox:
                                spacing 20
                                $ array_of_my_weapons = []
                                $ weaponOrEquipment_type = "w"                                
                                $ empty_scaled = im.Scale("images/background_item.png", scale, scale)
                                for my_protector in my_protectors_map.values():
                                    if my_protector.equipedWeapon != None:
                                        $ weapon = my_protector.equipedWeapon
                                        $ equipedProtectorWeapon = {
                                            "weapon": weapon,
                                            "protector": my_protector
                                        }
                                        $ array_of_my_weapons.append(equipedProtectorWeapon)
                                $ filtered_weapons = sorted(
                                    [weapon for weapon in myWeapons],
                                    key=lambda weapon: weapon.rarity
                                )
                                for weapon in filtered_weapons:
                                    $ unequipedWeapon = {
                                        "weapon": weapon
                                    }
                                    $ array_of_my_weapons.append(unequipedWeapon)
                                
                                for i in range(0, len(array_of_my_weapons), 4):
                                    hbox:
                                        xalign 0.5
                                        xfill True
                                        spacing 10  # space between columns
                                        for weapon_map in array_of_my_weapons[i:i+4]:
                                            $ weapon = weapon_map["weapon"]
                                            $ my_color = EClassColor
                                            $ rarity = weapon.rarity
                                            if weapon.rarity == "D":
                                                $ my_color = DClassColor
                                            if weapon.rarity == "C":
                                                $ my_color = CClassColor
                                            if weapon.rarity == "B":
                                                $ my_color = BClassColor
                                            if weapon.rarity == "A":
                                                $ my_color = AClassColor
                                            if weapon.rarity == "S":
                                                $ my_color = SClassColor

                                            $ weapon_img = "images/weapons/{}.png".format(weapon.type)

                                            # Get original image size
                                            $ orig_width, orig_height = renpy.image_size(weapon_img)

                                            # Calculate proportional width
                                            $ new_width = int(orig_width * (scale / float(orig_height)))

                                            # Scale the image
                                            $ weapon_scaled = im.Scale(weapon_img, new_width, scale)
                                            if weapon_map.get("protector") is None:
                                                $ button_action = Show("equipment_detail_screen", None, weaponOrEquipment_type, weapon)
                                            else:
                                                $ button_action = Show("equipment_detail_screen", None, weaponOrEquipment_type, weapon, weapon_map["protector"])
                                            vbox:
                                                xalign 0.5
                                                
                                                vbox:
                                                    xalign 0.5
                                                    button:
                                                        action button_action
                                                        xpadding 4
                                                        ypadding 4
                                                        frame:                                            
                                                            background my_color
                                                            xalign 0.5 
                                                            add im.Composite(
                                                                (scale, scale),
                                                                (0, 0), empty_scaled,
                                                                ((scale - new_width) // 2, 0), weapon_scaled   
                                                            )
                                            
                                                vbox:
                                                    xalign 0.5
                                                    if weapon_map.get("protector") is None:
                                                        button:
                                                            background "#00000020"
                                                            padding (5, 5)
                                                            action button_action

                                                            text "{} ({})".format(weapon.name, rarity):
                                                                size 30
                                                                xalign 0.5 
                                                                color my_color
                                                                line_spacing 0
                                                    else:
                                                        $ weapon_name = "{{size=30}}{{color={}}}{} ({}){{/color}}{{/size}}".format(my_color, weapon.name, rarity)
                                                        $ protector_name = "{{size=23}}Equiped by {}{{/size}}".format(my_protector.name)
                                                        button:
                                                            background "#00000020"
                                                            padding (5, 5)
                                                            action button_action
                                                            text "[weapon_name]\n[protector_name]":
                                                                xalign 0.5 
                                                                text_align 0.5
                                                                line_spacing 0
                                

screen my_equipments_screen():
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 300
        $ buttons_background = im.Scale("images/background_item.png", scale, scale)

        # Close button - top right
        textbutton "Back" action Hide("my_equipments_screen"):
            text_style "hover_white"
            xalign 1.0
            yalign 0.0
            padding (10, 5)
        vbox:
            spacing 50
            xalign 0.5
            yalign 0.1
            
            null height 10
            text "Equipments" size 50 color "#FFF" xalign 0.5

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                vbox:
                    spacing 20

                    frame:
                        xalign 0.0
                        yalign 0.0
                        padding (10, 10)
                        background Solid("#000000f1")
                        has vbox
                        
                        # Scrollable quest list
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            vbox:
                                spacing 20 
                                $ array_of_my_equipments = []
                                $ empty_scaled = im.Scale("images/background_item.png", scale, scale)
                                $ weaponOrEquipment_type = "e"
                                for my_protector in my_protectors_map.values():
                                    if my_protector.equipedHelmet != None:
                                        $ equipment = my_protector.equipedHelmet
                                        $ equipedEquipment = {
                                            "equipment": equipment,
                                            "protector": my_protector
                                        }
                                        $ array_of_my_equipments.append(equipedEquipment)
                                                
                                    if my_protector.equipedBodyArmor != None:
                                        $ equipment = my_protector.equipedBodyArmor
                                        $ equipedEquipment = {
                                            "equipment": equipment,
                                            "protector": my_protector
                                        }
                                        $ array_of_my_equipments.append(equipedEquipment)
                                    if my_protector.equipedPants != None:
                                        $ equipment = my_protector.equipedPants
                                        $ equipedEquipment = {
                                            "equipment": equipment,
                                            "protector": my_protector
                                        }
                                        $ array_of_my_equipments.append(equipedEquipment)
                                    if my_protector.equipedBoots != None:
                                        $ equipment = my_protector.equipedBoots
                                        $ equipedEquipment = {
                                            "equipment": equipment,
                                            "protector": my_protector
                                        }
                                        $ array_of_my_equipments.append(equipedEquipment)
                                $ filtered_equipments = sorted(
                                    [equipment for equipment in myEquipments],
                                    key=lambda equipment: equipment.rarity
                                )
                                for equipment in filtered_equipments:
                                    $ unequipedEquipment = {
                                        "equipment": equipment
                                    }
                                    $ array_of_my_equipments.append(unequipedEquipment)
                                
                                for i in range(0, len(array_of_my_equipments), 4):
                                    hbox:
                                        xalign 0.5
                                        xfill True
                                        spacing 10  # space between columns
                                        for equipment_map in array_of_my_equipments[i:i+4]:
                                            $ equipment = equipment_map["equipment"]
                                            $ my_color = EClassColor
                                            $ rarity = equipment.rarity
                                            if equipment.rarity == "D":
                                                $ my_color = DClassColor
                                            if equipment.rarity == "C":
                                                $ my_color = CClassColor
                                            if equipment.rarity == "B":
                                                $ my_color = BClassColor
                                            if equipment.rarity == "A":
                                                $ my_color = AClassColor
                                            if equipment.rarity == "S":
                                                $ my_color = SClassColor

                                            $ equipment_img = "images/equipments/{}_{}.png".format(equipment.class_name, equipment.type)

                                            # Get original image size
                                            $ orig_width, orig_height = renpy.image_size(equipment_img)

                                            # Calculate proportional width
                                            $ new_width = int(orig_width * (scale / float(orig_height)))

                                            # Scale the image
                                            $ equipment_scaled = im.Scale(equipment_img, new_width, scale)
                                            if equipment_map.get("protector") is None:
                                                $ button_action = Show("equipment_detail_screen", None, weaponOrEquipment_type, equipment)
                                            else:
                                                $ button_action = Show("equipment_detail_screen", None, weaponOrEquipment_type, equipment, equipment_map["protector"])
                                            vbox:
                                                xalign 0.5
                                                
                                                vbox:
                                                    xalign 0.5
                                                    button:
                                                        action button_action
                                                        xpadding 4
                                                        ypadding 4
                                                        frame:                                            
                                                            background my_color
                                                            xalign 0.5 
                                                            add im.Composite(
                                                                (scale, scale),
                                                                (0, 0), empty_scaled,
                                                                ((scale - new_width) // 2, 0), equipment_scaled   
                                                            )
                                            
                                                vbox:
                                                    xalign 0.5
                                                    if equipment_map.get("protector") is None:
                                                        button:
                                                            background "#00000020"
                                                            padding (5, 5)
                                                            action button_action

                                                            text "{} ({})".format(equipment.name, rarity):
                                                                size 30
                                                                xalign 0.5 
                                                                color my_color
                                                                line_spacing 0
                                                    else:
                                                        $ equipment_name = "{{size=30}}{{color={}}}{} ({}){{/color}}{{/size}}".format(my_color, equipment.name, rarity)
                                                        $ protector_name = "{{size=23}}Equiped by {}{{/size}}".format(my_protector.name)
                                                        button:
                                                            background "#00000020"
                                                            padding (5, 5)
                                                            action button_action
                                                            text "[equipment_name]\n[protector_name]":
                                                                xalign 0.5 
                                                                text_align 0.5
                                                                line_spacing 0


screen my_protectors_screen():
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 300

        $ buttons_background = im.Scale("images/background_item.png", scale, scale)
        

        # Close button - top right
        textbutton "Back" action Hide("my_protectors_screen"):
            text_style "hover_white"
            xalign 1.0
            yalign 0.0
            padding (10, 5)
        vbox:
            spacing 50
            null height 10
            text "Protectors" size 50 color "#FFF" xalign 0.5

            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True

                frame:
                    xalign 0.0
                    yalign 0.0
                    padding (10, 10)
                    background Solid("#000000f1")
                    has vbox
                    spacing 20
                    # Scrollable quest list
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        vbox:
                            spacing 20
                            $ protectors_list = list(my_protectors_map.values())
                            for i in range(0, len(protectors_list), 4):
                                hbox:
                                    xalign 0.5
                                    xfill True
                                    spacing 10  # space between columns
                                    for my_protector in protectors_list[i:i+4]:
                                        $ my_color = "#FFFFFF"
                                        $ message = my_protector.status
                                        if my_protector.readyForPromotion:
                                            $ my_color = "#ff0000"
                                            $ message = "Ready for promotion"
                                        if my_protector.status == "In a mission":
                                            $ my_color = "#1E3A8A"
                                            $ message = my_protector.status
                                        if my_protector.status == "Training":
                                            $ my_color = "#FACC15"
                                            $ message = my_protector.status

                                        $ image_name = my_protector.stage
                                        if my_protector.stage >= 5:
                                            $ image_name = str(my_protector.stage) + "_" + str(my_protector.chosen_evolution)

                                        # Path to the image
                                        $ show_protectors_image = "images/protectors/{}/{}.png".format(my_protector.name, image_name)

                                        # Get original image size
                                        $ orig_width, orig_height = renpy.image_size(show_protectors_image)

                                        # Calculate proportional width
                                        $ new_width = int(orig_width * (scale / float(orig_height)))

                                        # Scale the image
                                        $ show_protectors_scaled = im.Scale(show_protectors_image, new_width, scale)

                                        $ button_action = Show("protector_detail_screen", my_protector=my_protector)
                                        
                                        vbox:
                                            xalign 0.5
                                            vbox:
                                                xalign 0.5
                                                button:
                                                    action button_action
                                                    frame:
                                                        xalign 0.5 
                                                        add im.Composite(
                                                            (scale, scale),
                                                            (0, 0), buttons_background,
                                                            ((scale - new_width) // 2, 0), show_protectors_scaled
                                                            
                                                        )

                                            vbox:
                                                xalign 0.5
                                                button:
                                                    background "#00000020"
                                                    padding (5, 5)
                                                    action button_action
                                                    text "{} ({})".format(my_protector.name, message):
                                                        size 30
                                                        xalign 0.5 
                                                        color my_color
                                                        line_spacing 0

screen menu_button_for_protectors_game():
    if show_things:
        $ button_style = "hover_white"
        textbutton "Menu":
            text_style button_style
            background "#4448"
            xalign 0.5
            yalign 0.0
            padding (20, 10)
            text_size 40
            action Show("menu_for_protectors_game")

screen menu_for_protectors_game():
    frame:
        modal True
        background Solid(black_see_through_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 300

        $ buttons_background = im.Scale("images/background_item.png", scale, scale)

        fixed:
            xfill True
            yfill True

            # Close button - top right
            textbutton "Close" action Hide("menu_for_protectors_game"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
            vbox:
                yalign 0.1
                xalign 0.5
                text "Menu" size 50 color "#FFF" xalign 0.5
            vbox:
                yalign 0.5
                xalign 0.5
                spacing 50
                hbox:
                    yalign 0.5
                    xalign 0.5
                    spacing 100
                    
                    vbox:
                        spacing 20
                        $ show_protectors_image = "images/menu/protectors.png"
                        $ show_protectors_scaled = im.Scale(show_protectors_image, scale, scale)
                            
                        button:
                            action Show("my_protectors_screen")  # show possible weapons to use
                            background "#ffffff"
                            frame:
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), buttons_background,
                                    (0, 0), show_protectors_scaled
                                )
                        text "Protectors" color "#FFF" xalign 0.5
                    
                    vbox:
                        spacing 20
                        $ show_weapons_image = "images/menu/weapons.png"
                        $ show_weapons_scaled = im.Scale(show_weapons_image, scale, scale)
                            
                        button:
                            action Show("my_weapons_screen")  # show possible weapons to use
                            background "#ffffff"
                            frame:
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), buttons_background,
                                    (0, 0), show_weapons_scaled
                                )
                        text "Weapons" color "#FFF" xalign 0.5
                    
                    vbox:
                        spacing 20
                        $ show_equipment_image = "images/menu/equipments.png"
                        $ show_equipment_scaled = im.Scale(show_equipment_image, scale, scale)
                            
                        button:
                            action Show("my_equipments_screen")  # show possible weapons to use
                            background "#ffffff"
                            frame:
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), buttons_background,
                                    (0, 0), show_equipment_scaled
                                )
                        text "Equipments" color "#FFF" xalign 0.5


screen current_day_screen():
    if show_things:
        textbutton "Day: {}".format(current_day):
            xalign 0.0
            yalign 0.0
            padding (20, 10)
            background "#4448"
            text_color "b3b3b3"
            text_size 40

screen money_screen():
    if show_things:
        textbutton "{} $".format(money):
            xalign 1.0
            yalign 0.0
            padding (20, 10)
            background "#4448"
            text_color "b3b3b3"
            text_size 40

screen equipment_detail_screen(weaponOrEquipment_type, equipment_or_weapon, protector = None):
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 600

        fixed:
            xfill True
            yfill True

            # Close button - top right
            textbutton "Back" action Hide("equipment_detail_screen"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
            vbox:
                yalign 0.1
                xalign 0.5
                text "[equipment_or_weapon.name] ([equipment_or_weapon.rarity])" size 50 color "#FFF" xalign 0.5
            vbox:
                spacing 20
                xalign 0.9
                yalign 0.5
                $ background = im.Scale("images/background_item.png", scale, scale)

                
                if weaponOrEquipment_type == "w":
                    $ e_or_w_image = "images/weapons/{}.png".format(equipment_or_weapon.type)
                elif weaponOrEquipment_type == "e":
                    $ e_or_w_image = "images/equipments/{}_{}.png".format(equipment_or_weapon.class_name, equipment_or_weapon.type)

                # Get original image size
                $ orig_width, orig_height = renpy.image_size(e_or_w_image)

                # Calculate proportional width
                $ new_width = int(orig_width * (scale / float(orig_height)))

                # Scale the image
                $ e_or_w_scaled = im.Scale(e_or_w_image, new_width, scale)

                $ my_color = EClassColor
                $ rarity = equipment_or_weapon.rarity
                if equipment_or_weapon.rarity == "D":
                    $ my_color = DClassColor
                if equipment_or_weapon.rarity == "C":
                    $ my_color = CClassColor
                if equipment_or_weapon.rarity == "B":
                    $ my_color = BClassColor
                if equipment_or_weapon.rarity == "A":
                    $ my_color = AClassColor
                if equipment_or_weapon.rarity == "S":
                    $ my_color = SClassColor
                frame:                           
                    background my_color
                    xalign 0.5 
                    add im.Composite(
                        (scale, scale),
                        (0, 0), background,
                        ((scale - new_width) // 2, 0), e_or_w_scaled
                        
                    )
            vbox:
                spacing 20
                xalign 0.1
                yalign 0.5
                xmaximum 800
                text "[equipment_or_weapon.name] ([equipment_or_weapon.rarity])" size 25 color "#FFF" 
                text "[str(equipment_or_weapon.description)]" size 22 color "#EEE"
                null height 20
                hbox:
                    xalign 0.5
                    spacing 20
                    
                    
                    vbox:
                        xminimum 300
                        xalign 0.5
                        if protector is not None:
                            text "Equiped on:" size 22 color "#EEE"
                        text "Type:" size 22 color "#EEE"
                        text "Class:" size 22 color "#EEE"
                        if weaponOrEquipment_type == "w":
                            text "Base damage:" size 22 color "#EEE"
                            text "Range type:" size 22 color "#EEE"

                        elif weaponOrEquipment_type == "e":
                            text "Defense value:" size 22 color "#EEE"
                            text "[str(stats_increment_map[equipment_or_weapon.class_name]['prio1'])]:" size 22 color "#EEE"
                            text "[str(stats_increment_map[equipment_or_weapon.class_name]['prio2'])]:" size 22 color "#EEE"

                        text "Rarity:" size 22 color "#EEE"
                        
                    vbox:
                        xminimum 300
                        xalign 0.5
                        if protector is not None:
                            text protector.name size 22 color "#EEE" xalign 1.0
                        text "[str(equipment_or_weapon.type)]" size 22 color "#EEE" xalign 1.0
                        text "[str(equipment_or_weapon.class_name)]" size 22 color "#EEE" xalign 1.0
                        if weaponOrEquipment_type == "w":
                            text "[str(int(equipment_or_weapon.base_damage))]" size 22 color "#EEE" xalign 1.0
                            text "[str(equipment_or_weapon.range)]" size 22 color "#EEE" xalign 1.0
                        elif weaponOrEquipment_type == "e":
                            text "[str(int(equipment_or_weapon.base_defense))]" size 22 color "#EEE" xalign 1.0
                            text "+[str(equipment_or_weapon.prio1)]%" size 22 color "#EEE" xalign 1.0
                            text "+[str(equipment_or_weapon.prio2)]%" size 22 color "#EEE" xalign 1.0
                        
                        text "[str(equipment_or_weapon.rarity)]" size 22 color "#EEE" xalign 1.0
                            
screen protector_evolution_choosing_screen(my_protector):
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 500
        $ buttons_background = im.Scale("images/background_item.png", scale, scale)
        fixed:
            xfill True
            yfill True

            # Close button - top right
            textbutton "Back" action Hide("protector_evolution_choosing_screen"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
            vbox:
                yalign 0.1
                xalign 0.5
                text "[my_protector.name]" size 50 color "#FFF" xalign 0.5
            hbox:
                xfill True
                xalign 0.5
                yalign 0.5
                vbox:
                    spacing 20
                    xalign 0.5
                    text str(my_protector.basePoints.evolution_name_1):
                        xalign 0.5
                    $ image_name = "5_1"

                    # Path to the image
                    $ show_protectors_image = "images/protectors/{}/{}.png".format(my_protector.name, image_name)

                    # Get original image size
                    $ orig_width, orig_height = renpy.image_size(show_protectors_image)

                    # Calculate proportional width
                    $ new_width = int(orig_width * (scale / float(orig_height)))

                    # Scale the image
                    $ show_protectors_scaled = im.Scale(show_protectors_image, new_width, scale)
                    button:
                        frame:
                            xalign 0.5 
                            add im.Composite(
                                (scale, scale),
                                (0, 0), buttons_background,
                                ((scale - new_width) // 2, 0), im.Flip(show_protectors_scaled, horizontal=True)
                            )
                    text str(my_protector.basePoints.evolution_description_1):
                        xmaximum scale
                        size 25
                        xalign 0.5
                        text_align 0.5
                    textbutton str(my_protector.basePoints.evolution_name_1):
                        action Show("protector_evolution_detail_screen", None, my_protector, 1) 
                        text_style "button_in_black_background"
                        padding (10, 5)
                        xalign 0.5
                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    text "Choose wisely!":
                        color "#FFF"
                        size 30
                        xalign 0.5
                    text "You may only choose one":
                        color "#FFF"
                        size 25
                        xalign 0.5
                vbox:
                    spacing 20
                    xalign 0.5
                    text str(my_protector.basePoints.evolution_name_2):
                        xalign 0.5
                    $ image_name = "5_2"

                    # Path to the image
                    $ show_protectors_image = "images/protectors/{}/{}.png".format(my_protector.name, image_name)

                    # Get original image size
                    $ orig_width, orig_height = renpy.image_size(show_protectors_image)

                    # Calculate proportional width
                    $ new_width = int(orig_width * (scale / float(orig_height)))

                    # Scale the image
                    $ show_protectors_scaled = im.Scale(show_protectors_image, new_width, scale)
                    button:
                        frame:
                            xalign 0.5 
                            add im.Composite(
                                (scale, scale),
                                (0, 0), buttons_background,
                                ((scale - new_width) // 2, 0), show_protectors_scaled
                                
                            )
                    text str(my_protector.basePoints.evolution_description_2):
                        xmaximum scale
                        size 25
                        xalign 0.5
                        text_align 0.5
                    textbutton str(my_protector.basePoints.evolution_name_2):
                        action Show("protector_evolution_detail_screen", None, my_protector, 2) 
                        text_style "button_in_black_background"
                        padding (10, 5)
                        xalign 0.5

screen protector_evolution_detail_screen(my_protector, evolution):
    $ protector_evolution_name = my_protector.basePoints.evolution_name_1
    if evolution == 2:
        $ protector_evolution_name = my_protector.basePoints.evolution_name_2
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 500
        fixed:
            xfill True
            yfill True

            # Close button - top right
            textbutton "Back" action Hide("protector_evolution_detail_screen"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
            vbox:
                yalign 0.1
                xalign 0.5
                text "[my_protector.name]" size 50 color "#FFF" xalign 0.5
            hbox:
                xfill True
                xalign 0.5
                yalign 0.5

                # getting the improvements array
                $ evolution_parameter_key = "evolution_1"
                $ possible_future_weapons_array = my_protector.basePoints.usable_weapon_types_evolution_1
                if evolution == 2:
                    $ evolution_parameter_key = "evolution_2"
                    $ possible_future_weapons_array = my_protector.basePoints.usable_weapon_types_evolution_2
                $ evolution_parameter = getattr(my_protector.basePoints, evolution_parameter_key)
                $ increase_array = evolution_increment_map[evolution_parameter]["increase"]
                $ decrease_array = evolution_increment_map[evolution_parameter]["decrease"]
                
                # getting the number of increasing att we are going to get
                $ number_of_improvements = len(increase_array)
                $ increasing_percentage = int(percentage_for_increasing_on_evolutions * 100 / number_of_improvements)

                # getting the number of decreasing att we are going to get
                $ number_of_improvements = len(decrease_array)
                $ decreasing_percentage = 0
                if number_of_improvements != 0:
                    $ decreasing_percentage = int(percentage_for_decreasing_on_evolutions * 100 / number_of_improvements)

                $ str_t_color = "#EEE"
                $ con_t_color = "#EEE"
                $ wis_t_color = "#EEE"
                $ spe_t_color = "#EEE"
                $ dex_t_color = "#EEE"
                $ int_t_color = "#EEE"
                $ cha_t_color = "#EEE"
                $ luc_t_color = "#EEE"

                $ current_stats = my_protector.get_current_stats(5, None)
                $ evolution_stats = my_protector.get_current_stats(5, evolution)

                $ str_text = str(current_stats['strength'])
                $ con_text = str(current_stats['constitution'])
                $ wis_text = str(current_stats['wisdom'])
                $ spe_text = str(current_stats['speed'])
                $ dex_text = str(current_stats['dexterity'])
                $ int_text = str(current_stats['intelligence'])
                $ cha_text = str(current_stats['charisma'])
                $ luc_text = str(current_stats['luck'])

                if "Strength" in increase_array:
                    $ percentage_change = increasing_percentage * increase_array.count("Strength")
                    $ str_t_color = "#4CAF50"
                    $ str_text = str(current_stats['strength']) + " → " + str(evolution_stats['strength']) + " (+" + str(percentage_change) + "%)"
                elif "Strength" in decrease_array:
                    $ percentage_change = decreasing_percentage * decrease_array.count("Strength")
                    $ str_t_color = "#F44336"
                    $ str_text = str(current_stats['strength']) + " → " + str(evolution_stats['strength']) + " (-" + str(percentage_change) + "%)"
                if "Constitution" in increase_array:
                    $ percentage_change = increasing_percentage * increase_array.count("Constitution")
                    $ con_t_color = "#4CAF50"
                    $ con_text = str(current_stats['constitution']) + " → " + str(evolution_stats['constitution']) + " (+" + str(percentage_change) + "%)"
                elif "Constitution" in decrease_array:
                    $ percentage_change = decreasing_percentage * decrease_array.count("Constitution")
                    $ con_t_color = "#F44336"
                    $ con_text = str(current_stats['constitution']) + " → " + str(evolution_stats['constitution']) + " (-" + str(percentage_change) + "%)"
                if "Wisdom" in increase_array:
                    $ percentage_change = increasing_percentage * increase_array.count("Wisdom")
                    $ wis_t_color = "#4CAF50"
                    $ wis_text = str(current_stats['wisdom']) + " → " + str(evolution_stats['wisdom']) + " (+" + str(percentage_change) + "%)"
                elif "Wisdom" in decrease_array:
                    $ percentage_change = decreasing_percentage * decrease_array.count("Wisdom")
                    $ wis_t_color = "#F44336"
                    $ wis_text = str(current_stats['wisdom']) + " → " + str(evolution_stats['wisdom']) + " (-" + str(percentage_change) + "%)"
                if "Speed" in increase_array:
                    $ percentage_change = increasing_percentage * increase_array.count("Speed")
                    $ spe_t_color = "#4CAF50"
                    $ spe_text = str(current_stats['speed']) + " → " + str(evolution_stats['speed']) + " (+" + str(percentage_change) + "%)"
                elif "Speed" in decrease_array:
                    $ percentage_change = decreasing_percentage * decrease_array.count("Speed")
                    $ spe_t_color = "#F44336"
                    $ spe_text = str(current_stats['speed']) + " → " + str(evolution_stats['speed']) + " (-" + str(percentage_change) + "%)"
                if "Dexterity" in increase_array:
                    $ percentage_change = increasing_percentage * increase_array.count("Dexterity")
                    $ dex_t_color = "#4CAF50"
                    $ dex_text = str(current_stats['dexterity']) + " → " + str(evolution_stats['dexterity']) + " (+" + str(percentage_change) + "%)"
                elif "Dexterity" in decrease_array:
                    $ percentage_change = decreasing_percentage * decrease_array.count("Dexterity")
                    $ dex_t_color = "#F44336"
                    $ dex_text = str(current_stats['dexterity']) + " → " + str(evolution_stats['dexterity']) + " (-" + str(percentage_change) + "%)"
                if "Intelligence" in increase_array:
                    $ percentage_change = increasing_percentage * increase_array.count("Intelligence")
                    $ int_t_color = "#4CAF50"
                    $ int_text = str(current_stats['intelligence']) + " → " + str(evolution_stats['intelligence']) + " (+" + str(percentage_change) + "%)"
                elif "Intelligence" in decrease_array:
                    $ percentage_change = decreasing_percentage * decrease_array.count("Intelligence")
                    $ int_t_color = "#F44336"
                    $ int_text = str(current_stats['intelligence']) + " → " + str(evolution_stats['intelligence']) + " (-" + str(percentage_change) + "%)"
                if "Charisma" in increase_array:
                    $ percentage_change = increasing_percentage * increase_array.count("Charisma")
                    $ cha_t_color = "#4CAF50"
                    $ cha_text = str(current_stats['charisma']) + " → " + str(evolution_stats['charisma']) + " (+" + str(percentage_change) + "%)"
                elif "Charisma" in decrease_array:
                    $ percentage_change = decreasing_percentage * decrease_array.count("Charisma")
                    $ cha_t_color = "#F44336"
                    $ cha_text = str(current_stats['charisma']) + " → " + str(evolution_stats['charisma']) + " (-" + str(percentage_change) + "%)"
                if "Luck" in increase_array:
                    $ percentage_change = increasing_percentage * increase_array.count("Luck")
                    $ luc_t_color = "#4CAF50"
                    $ luc_text = str(current_stats['luck']) + " → " + str(evolution_stats['luck']) + " (+" + str(percentage_change) + "%)"
                elif "Luck" in decrease_array:
                    $ percentage_change = decreasing_percentage * decrease_array.count("Luck")
                    $ luc_t_color = "#F44336"
                    $ luc_text = str(current_stats['luck']) + " → " + str(evolution_stats['luck']) + " (-" + str(percentage_change) + "%)"

                vbox:
                    xalign 0.2
                    yalign 0.5
                    spacing 45
                    text str(protector_evolution_name):
                        xalign 0.5
                        size 40
                        color "#EEE"
                    vbox:
                        spacing 20
                        xalign 0.5
                        text "Final attributes:":
                            xalign 0.5
                        hbox:
                            xalign 0.5
                            spacing 20
                            $ size_letter = 25
                            vbox:
                                xalign 0.5
                                text "Strength:" size size_letter color str_t_color
                                text "Constitution:" size size_letter color con_t_color
                                text "Wisdom:" size size_letter color wis_t_color
                                text "Speed:" size size_letter color spe_t_color
                            vbox:
                                xalign 0.5
                                text "[str_text]" size size_letter color str_t_color
                                text "[con_text]" size size_letter color con_t_color
                                text "[wis_text]" size size_letter color wis_t_color
                                text "[spe_text]" size size_letter color spe_t_color
                            vbox:
                                null width 40  # This adds 40 pixels of vertical space at the top
                            vbox:
                                xalign 0.5
                                text "Dexterity:" size size_letter color dex_t_color
                                text "Intelligence:" size size_letter color int_t_color
                                text "Charisma:" size size_letter color cha_t_color
                                text "Luck:" size size_letter color luc_t_color
                            vbox:
                                xalign 0.5
                                text "[dex_text]" size size_letter color dex_t_color
                                text "[int_text]" size size_letter color int_t_color
                                text "[cha_text]" size size_letter color cha_t_color
                                text "[luc_text]" size size_letter color luc_t_color
                    vbox:
                        spacing 20
                        xalign 0.5
                        text "Usable weapons:":
                            xalign 0.5
                        vbox:
                            xalign 0.5
                            spacing 20
                            for i in range(0, len(possible_future_weapons_array), 6):
                                hbox:
                                    xalign 0.5
                                    spacing 20
                                    for weapon_type in possible_future_weapons_array[i:i+6]:
                                        text [weapon_type] size 25 color "#EEE" xalign 0.5
                            if my_protector.equipedWeapon != None:                                        
                                if my_protector.equipedWeapon.type not in possible_future_weapons_array:
                                    text "Warning: Current weapon will be removed from the protector.\n It will be stored in your inventory." size 22 color "#FFD700" xalign 0.5 text_align 0.5
                            

            $ image_name = "5_" + str(evolution)

            python:
                image_name = "5_" + str(evolution)
                image_path = getImage(str(get_folder_from_map(my_protector.name)) + '/' + str(image_name))
                if image_path:
                    ui.at(right)
                    ui.at(fit_to_screen_height)
                    ui.add(image_path)
                            
            vbox:
                yalign 0.9
                xalign 0.5
                textbutton "Choose: " + str(protector_evolution_name):
                    action [Function(update_evolution_for_protector, my_protector, evolution), 
                            Hide("protector_evolution_detail_screen"), Hide("protector_evolution_choosing_screen")] 
                    text_style "button_in_black_background"
                    padding (10, 5)
                    xalign 0.5

screen protector_selection(isThisExpedition):
    if isThisExpedition:
        $ where_to = "send_to_mission"
    else:
        $ where_to = "send_to_training"
    tag menu

    # Full-screen container to allow positioning in center
    frame:
        xalign 0.5
        yalign 0.5
        padding (100, 50)
        style_prefix "menu"

        vbox:
            spacing 10
            align (0.5, 0.5)

            label "Choose a protector to train" xalign 0.5
            if allExpeditions[0].status != "started":
                $ has_available = False
                for key, protector in my_protectors_map.items():
                    if protector.status == "Available":
                        $ has_available = True
                        textbutton protector.name + ' (' + str(protector.status) + ')' xalign 0.5 action [SetVariable("selected_protector", protector), Jump(where_to)]

                if not has_available:
                    text "No protectors are currently available." xalign 0.5
            else: 
                text "Training facility already occupied with: [my_protectors_map[allExpeditions[0].assignedProtectorName].name] " xalign 0.5
            textbutton "Back" action Return():
                text_style "hover_black"
                xalign 0.5

screen expedition_screen(regionNumber):
    $ min_level = (regionNumber - 1) * 20
    $ max_level = regionNumber * 20
    default page = 0
    default page_size = 5
    default filtered_expeditions = [m for m in allExpeditions if min_level <= m.difficulty <= max_level and m.title != "Training"]
    default max_pages = max((len(filtered_expeditions) - 1) // page_size, 0)
    default mode = "list"
    default selected_expedition = None
    default selected_boss_expedition = None
    
    # List of available protectors
    $ available_protectors = [p for p in my_protectors_map.values() if p.status == "Available"]
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        
        ysize 925
        padding (20, 20)
        vbox:
            xsize 700
            xalign 0.5  # center content inside the frame
            if mode == "list":
                vbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.0
                    vbox:
                        xalign 0.5
                        vbox:
                            xalign 0.5
                            text "Expeditions" size 40
                        
                        vbox:
                            xalign 0.5
                            $ bossExpedition = next((m for m in bossExpeditions if m.regionNumber == regionNumber), None)
                            vbox:
                                xalign 0.5
                                yminimum 75
                                if bossExpedition.successfulMinorExpeditions >= bossExpedition.successfulMinorExpeditionsRequired:
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        spacing 5
                                        textbutton "❗Boss Fight❗" text_size 27 action [SetScreenVariable("mode", "boss_fight_detail"), SetScreenVariable("selected_boss_expedition", bossExpedition)] style "background_boss_expedition_button" text_style "text_boss_expedition_button"
                                else:
                                    bar value bossExpedition.successfulMinorExpeditions range bossExpedition.successfulMinorExpeditionsRequired:
                                        xmaximum 400
                                        ymaximum 30

                                    vbox:
                                        xalign 0.5
                                        text "[bossExpedition.successfulMinorExpeditions] / [bossExpedition.successfulMinorExpeditionsRequired]" size 24

                    for i in range(page * page_size, min((page + 1) * page_size, len(filtered_expeditions))):
                        $ expedition = filtered_expeditions[i]
                        button:
                            xfill True
                            frame:
                                xfill True
                                style "background_expedition_button"
                                padding (10, 10)
                                vbox:
                                    spacing 5
                                    text "[expedition.title] ([expedition.expedition_type])" size 24 color "#fff"
                                    text expedition.description size 16 color "#ccc"
                                    text "Difficulty: [expedition.difficulty]" size 14 color "#aaa"
                            action [SetScreenVariable("mode", "detail"), SetScreenVariable("selected_expedition", expedition)]

                    hbox:
                        spacing 20
                        xalign 0.5

                        if page > 0:
                            textbutton "Previous" action SetScreenVariable("page", page - 1) text_size 25
                        else:
                            textbutton "Previous" action NullAction() sensitive False text_size 25

                        if page < max_pages:
                            textbutton "Next" action SetScreenVariable("page", page + 1) text_size 25
                        else:
                            textbutton "Next" action NullAction() sensitive False text_size 25

                    textbutton "Return" action Return() xalign 0.5 text_size 25

            elif mode == "detail" and selected_expedition is not None:
                vbox:
                    yalign 0.0
                    xalign 0.5
                    spacing 20
                    xsize 700
                    null height 40  # This adds 40 pixels of vertical space at the top
                    
                    vbox:
                        xalign 0.5
                        text "[selected_expedition.title]" size 40 color "#000000"
                        
                        vbox:
                            xalign 0.5
                            spacing 20
                            text "([selected_expedition.expedition_type])" size 30 color "#000000"
                        
                            vbox:
                                xalign 0.5
                                text "Difficulty: [selected_expedition.difficulty]" size 20 color "#5a5a5a"

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    text selected_expedition.description size 20 color "#5a5a5a" xalign 0.5

                    $ neededDaysToFinish_day_name = "day"
                    $ disapearingInThisDays_day_name = "day"
                    if selected_expedition.neededDaysToFinish > 1:
                        $ neededDaysToFinish_day_name = "days"
                    if selected_expedition.disapearingInThisDays > 1:
                        $ disapearingInThisDays_day_name = "days"
                        
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top
                    hbox:
                        xsize 700
                        spacing 20

                        vbox:
                            xalign 0.2  # force to left
                            spacing 20

                            hbox:
                                text "Payment:" size 18 color "#5a5a5a"
                            hbox:
                                text "Time it takes to complete:" size 18 color "#5a5a5a"
                            if selected_expedition.status != "started":
                                hbox:
                                    text "Will disappear in:" size 18 color "#5a5a5a"
                            if selected_expedition.status == "assigned":
                                hbox:
                                    text "Assigned protector:" size 18 color "#5a5a5a"

                        vbox:
                            xalign 0.8  # force to right
                            spacing 20

                            hbox:
                                xalign 1.0  # force to right
                                text "[selected_expedition.gold_received] $" size 18 color "#5a5a5a"
                            hbox:
                                xalign 1.0  # force to right
                                text "[selected_expedition.neededDaysToFinish] [neededDaysToFinish_day_name]" size 18 color "#5a5a5a"
                            if selected_expedition.status != "started":
                                hbox:
                                    xalign 1.0  # force to right
                                    text "[selected_expedition.disapearingInThisDays] [disapearingInThisDays_day_name]" size 18 color "#5a5a5a"
                            if selected_expedition.status == "assigned":
                                hbox:
                                    xalign 1.0  # force to right
                                    text "[selected_expedition.assignedProtectorName]" size 18 color "#5a5a5a"
                
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    if selected_expedition.status == "assigned":
                        $ success_rate = selected_expedition.get_success_rate(my_protectors_map[selected_expedition.assignedProtectorName])
                        if success_rate > 100:
                            $ success_rate = 100
                        vbox: 
                            xalign 0.5
                            spacing 10
                            bar value success_rate range 100 style "success_rate_bar"
                            text "Success rate: [success_rate] %" size 20 xalign 0.5
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    if selected_expedition.status != "started":
                        if selected_expedition.assignedProtectorName == None:
                            hbox:
                                xalign 0.5
                                spacing 10
                                for protector in available_protectors:
                                    $ select_protector_button_style = "button_small_text"
                                    if protector.name == selected_expedition.assignedProtectorName:
                                        $ select_protector_button_style = "button_small_text_selected"
                                    textbutton protector.name style str(select_protector_button_style) action Function(selected_expedition.assignProtector, protector.name) text_size 20

                                
                                if len(available_protectors) == 0:
                                    text "There are no available protectors." size 15 color "#5a5a5a" xmaximum 640
                        else:
                            hbox:
                                xalign 0.5
                                spacing 10
                                textbutton "Unassign [selected_expedition.assignedProtectorName]" action Function(selected_expedition.unassignProtector) text_size 20

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top
                    null ysize 1  # This adds 40 pixels of vertical space at the top
                    
                    hbox:
                        xalign 0.5
                        spacing 20
                        if selected_expedition.status != "started" and selected_expedition.assignedProtectorName != None:
                            textbutton "Start Expedition" action Function(selected_expedition.startExpedition, success_rate) text_size 25
                        textbutton "Back" action SetScreenVariable("mode", "list") text_size 25
            
            elif mode == "boss_fight_detail" and selected_boss_expedition is not None:
                vbox:
                    yalign 0.0
                    xalign 0.5
                    spacing 20
                    xsize 700
                    null height 40  # This adds 40 pixels of vertical space at the top
                    
                    vbox:
                        xalign 0.5
                        text "[selected_boss_expedition.title]" size 40 color "#000000" xalign 0.5

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    text selected_boss_expedition.description size 20 color "#5a5a5a" xalign 0.5 text_align 0.5

                    hbox:
                        xsize 700
                        spacing 20
                        vbox:
                            xalign 0.2  # force to left
                            spacing 20

                            hbox:
                                text "Payment:" size 18 color "#5a5a5a"
                            if selected_boss_expedition.status == "assigned":
                                hbox:
                                    text "Assigned protector:" size 18 color "#5a5a5a"

                        vbox:
                            xalign 0.8  # force to right
                            spacing 20

                            hbox:
                                xalign 1.0  # force to right
                                text "[selected_boss_expedition.gold_received] $" size 18 color "#5a5a5a"
                            if selected_boss_expedition.status == "assigned":
                                hbox:
                                    xalign 1.0  # force to right
                                    text "[selected_boss_expedition.assignedProtectorName]" size 18 color "#5a5a5a"

                    if selected_boss_expedition.assignedProtectorName == None:
                        hbox:
                            xalign 0.5
                            spacing 10
                            for protector in available_protectors:
                                $ select_protector_button_style = "button_small_text"
                                if protector.name == selected_boss_expedition.assignedProtectorName:
                                    $ select_protector_button_style = "button_small_text_selected"
                                textbutton protector.name style str(select_protector_button_style) action Function(selected_boss_expedition.assignProtector, protector.name) text_size 20

                            
                            if len(available_protectors) == 0:
                                text "There are no available protectors." size 15 color "#5a5a5a" xmaximum 640
                    else:
                        hbox:
                            xalign 0.5
                            spacing 10
                            textbutton "Unassign [selected_boss_expedition.assignedProtectorName]" action Function(selected_boss_expedition.unassignProtector) text_size 20
                        
                    hbox:
                        xalign 0.5
                        spacing 20
                        if selected_boss_expedition.assignedProtectorName != None:
                            textbutton "Start Boss Fight" action Function(selected_boss_expedition.startBossExpedition) text_size 25 
                        textbutton "Back" action SetScreenVariable("mode", "list") text_size 25

screen base_stats(baseProtectorObject):
    key config.keymap["hide_windows"] action None
    frame:
        background "#00000069"
        xalign 0.2
        yalign 0.5
        padding (50, 50)

        vbox:
            spacing 20
            text "Base Stats" size 30 xalign 0.5 color "#FFF"
            hbox:
                xalign 0.5
                spacing 50
                vbox:
                    spacing 30
                    xalign 0.5
                    text "Strength:" size 25 color "#EEE"
                    text "Constitution:" size 25 color "#EEE"
                    text "Wisdom:" size 25 color "#EEE"
                    text "Morality:" size 25 color "#EEE"
                vbox:
                    spacing 30
                    xalign 0.5
                    text "[str(baseProtectorObject.get_base_information()['strength'])]" size 25 color "#EEE"
                    text "[str(baseProtectorObject.get_base_information()['constitution'])]" size 25 color "#EEE"
                    text "[str(baseProtectorObject.get_base_information()['wisdom'])]" size 25 color "#EEE"
                    text "[str(baseProtectorObject.get_base_information()['morality'])]" size 25 color "#EEE"
                vbox:
                    spacing 30
                    xalign 0.5
                    text "Dexterity:" size 25 color "#EEE"
                    text "Intelligence:" size 25 color "#EEE"
                    text "Charisma:" size 25 color "#EEE"
                    text "Luck:" size 25 color "#EEE"
                vbox:
                    spacing 30
                    xalign 0.5
                    text "[str(baseProtectorObject.get_base_information()['dexterity'])]" size 25 color "#EEE"
                    text "[str(baseProtectorObject.get_base_information()['intelligence'])]" size 25 color "#EEE"
                    text "[str(baseProtectorObject.get_base_information()['charisma'])]" size 25 color "#EEE"
                    text "[str(baseProtectorObject.get_base_information()['luck'])]" size 25 color "#EEE"


screen weapon_base_stats(weaponObject):
    key config.keymap["hide_windows"] action None
    $ build = "Strength-focused protectors"
    if weaponObject.class_name == "Dexterity":
        $ build = "Dexterity-focused protectors"
    if weaponObject.class_name == "Magic":
        $ build = "Intelligence- and Wisdom-focused protectors"

    frame:
        background "#00000069"
        xalign 0.2
        yalign 0.5
        padding (50, 50)

        vbox:
            spacing 20
            text "Base Stats" size 30 xalign 0.5 color "#FFF"
            hbox:
                xalign 0.5
                spacing 50
                vbox:
                    spacing 30
                    xalign 0.5
                    text "Name:" size 25 color "#EEE"
                    text "Description:" size 25 color "#EEE"
                    text "Base damage:" size 25 color "#EEE"
                    text "Type:" size 25 color "#EEE"
                    text "Class:" size 25 color "#EEE"
                    text "Recommended to use on:" size 25 color "#EEE"
                vbox:
                    spacing 30
                    xalign 0.5
                    text "[str(weaponObject.name)]" size 25 color "#EEE"
                    text "[str(weaponObject.description)]" size 25 color "#EEE"
                    text "[str(weaponObject.base_damage)]" size 25 color "#EEE"
                    text "[str(weaponObject.type)]" size 25 color "#EEE"
                    text "[str(weaponObject.class_name)]" size 25 color "#EEE"
                    text "[str(build)]" size 25 color "#EEE"

screen weapon_select(protector):

    tag menu  # so the player can't open other menus while this is open

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

        vbox:
            spacing 10
            xalign 0.5
            text "Select your weapon:" size 30 xalign 0.5

            # For each available weapon, create a button
            $ filtered_weapons = sorted(
                [weapon for weapon in myWeapons if weapon.type in protector.basePoints.usable_weapon_types],
                key=lambda weapon: (weapon.rarity, weapon.name.lower())
            )
            for weapon in filtered_weapons:
                textbutton "[weapon.name] - [weapon.class_name] ([weapon.rarity])":
                    action [Function(protector.equip_weapon, weapon.weapon_id), Hide("weapon_select")]
                    ypadding 10
                    xalign 0.5

            textbutton "Cancel":
                action Hide("weapon_select")
                xalign 0.5
                ypadding 10

screen equipment_select(protector, equipment_type):

    tag menu  # so the player can't open other menus while this is open

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20

        vbox:
            spacing 10
            xalign 0.5

            text "Select your equipment:" size 30 xalign 0.5

            # For each available weapon, create a button
            $ filtered_equipments = sorted(
                [equipment for equipment in myEquipments if equipment.type == equipment_type],
                key=lambda equipment: (equipment.rarity, equipment.name.lower())
            )

            for equipment in filtered_equipments:
                textbutton "[equipment.name] - [equipment.class_name] ([equipment.rarity])":
                    action [Function(protector.equip_equipment, equipment.equipment_id), Hide("equipment_select")]
                    xalign 0.5
                    ypadding 10

            textbutton "Cancel":
                action Hide("equipment_select")
                ypadding 10
                xalign 0.5


screen lucky_box_screen(box_type):
    frame:
        modal True
        background Solid(black_see_through_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 650

        $ buttons_background = im.Scale("images/background_item.png", scale, scale)

        fixed:
            xfill True
            yfill True

            vbox:
                yalign 0.1
                xalign 0.5
                $ name = "Protector"
                $ lucky_box = "lucky_box_protector"
                
                if box_type == "Equipment":
                    $ name = "Equipment"
                    $ lucky_box = "lucky_box_equipment"
                elif box_type == "weapon":
                    $ name = "Weapon"
                    $ lucky_box = "lucky_box_weapon"
                text "[name] Lucky Box" size 50 color "#FFF" xalign 0.5
            vbox:
                yalign 0.5
                xalign 0.5
                spacing 50
                hbox:
                    yalign 0.5
                    xalign 0.5
                    spacing 100
                    $ show_protectors_image = "images/" + str(lucky_box) + ".png"
                    $ show_protectors_scaled = im.Scale(show_protectors_image, scale, scale)
                        
                    button:
                        action Function(lambda: open_protectors_box())
                        background "#ffffff"
                        frame:
                            add im.Composite(
                                (scale, scale),
                                (0, 0), buttons_background,
                                (0, 0), show_protectors_scaled
                            )

screen online_shop():
    
    # # Check if I already have the protector
    # #   -   if so, then it should not be available anymore
    $ online_shop_variable.checkIfProtectorStillAvailable()

    default online_shop_show = "main_menu"
    default rarity_selected = "S"
    $ online_shop_color = "#FFF"
    $ title_size = 60
    $ tittle_v_align = 0.1
    if online_shop_show != "main_menu":
        $ title_size = 40
        $ tittle_v_align = 0.01

    $ text_style_back_button = "rarity_navegation_text_online_shop"
    $ main_options_scale = 350
    $ items_scale = 400
    $ main_buttons_background = im.Scale("images/background_item.png", main_options_scale, main_options_scale)
    $ empty_scaled = im.Scale("images/background_item.png", items_scale, items_scale)
    frame:
        background Solid("#1a1a1a")
        fixed:
            xfill True
            yfill True
        xalign 0.5
        yalign 0.5
        xsize 1700
        
        ysize 925
        padding (20, 20)
        vbox:
            spacing 10
            xalign 1.0
            yalign 0                
            vbox:
                text "Next refresh: " + str(online_shop_refresh_in) + "d" size 20 color online_shop_color
        vbox:
            spacing 10
            xalign 0.5
            yalign tittle_v_align
            vbox:
                xalign 0.5
                
                vbox:
                    xalign 0.5
                    text "Online Shop" size title_size color online_shop_color

        vbox:
            spacing 10
            xalign 0.5
            yalign 0.5
            if online_shop_show == "main_menu":
                hbox:
                    spacing 50
                    xalign 0.5
                    yalign 0.5
                    $ show_protectors_image = "images/menu/protectors.png"
                    $ show_protectors_scaled = im.Scale(show_protectors_image, main_options_scale, main_options_scale)
                        
                    fixed: 
                        xmaximum main_options_scale
                        ymaximum main_options_scale
                        button:
                            action [SetScreenVariable("online_shop_show", "show_protectors"), SetVariable("online_shop_new_protectors", False) ]
                            style "option_button_online_shop"
                            frame:
                                add im.Composite(
                                    (main_options_scale, main_options_scale),
                                    (0, 0), main_buttons_background,
                                    (0, 0), show_protectors_scaled
                                )
                        if online_shop_new_protectors == True:
                            frame:
                                background "#fff"  # white background
                                padding (5, 2)    # space around the "!"
                                xalign 1.0
                                yalign 0.0
                                text "!" size 30 color "#f00" bold True

                    
                    $ show_weapons_image = "images/menu/weapons.png"
                    $ show_weapons_scaled = im.Scale(show_weapons_image, main_options_scale, main_options_scale)
                    
                    fixed: 
                        xmaximum main_options_scale
                        ymaximum main_options_scale
                        button:
                            action [SetScreenVariable("online_shop_show", "show_weapons"), SetVariable("online_shop_new_weapons", False)]
                            style "option_button_online_shop"
                            frame:
                                add im.Composite(
                                    (main_options_scale, main_options_scale),
                                    (0, 0), main_buttons_background,
                                    (0, 0), show_weapons_scaled
                                )
                        if online_shop_new_weapons == True:
                            frame:
                                background "#fff"  # white background
                                padding (5, 2)    # space around the "!"
                                xalign 1.0
                                yalign 0.0
                                text "!" size 30 color "#f00" bold True
                            

                    $ show_equipment_image = "images/menu/equipments.png"
                    $ show_equipment_scaled = im.Scale(show_equipment_image, main_options_scale, main_options_scale)
                        
                    fixed: 
                        xmaximum main_options_scale
                        ymaximum main_options_scale
                        button:
                            action [SetScreenVariable("online_shop_show", "show_equipments"), SetVariable("online_shop_new_equipments", False)]
                            style "option_button_online_shop"
                            frame:
                                add im.Composite(
                                    (main_options_scale, main_options_scale),
                                    (0, 0), main_buttons_background,
                                    (0, 0), show_equipment_scaled
                                )
                        if online_shop_new_equipments == True:
                            frame:
                                background "#fff"  # white background
                                padding (5, 2)    # space around the "!"
                                xalign 1.0
                                yalign 0.0
                                text "!" size 30 color "#f00" bold True

            if online_shop_show == "show_equipments":
                
                hbox:
                    spacing 50
                    xalign 0.5
                    yalign 0.5
                    for rarity, equipments in online_shop_variable.selling_equipments_list.items():
                        if rarity == rarity_selected:
                            for equipment in equipments:
                                $ my_color = EClassColor
                                $ rarity = equipment.rarity
                                if equipment.rarity == "D":
                                    $ my_color = DClassColor
                                if equipment.rarity == "C":
                                    $ my_color = CClassColor
                                if equipment.rarity == "B":
                                    $ my_color = BClassColor
                                if equipment.rarity == "A":
                                    $ my_color = AClassColor
                                if equipment.rarity == "S":
                                    $ my_color = SClassColor
                                
                                $ equipment_img = "images/equipments/{}_{}.png".format(equipment.class_name, equipment.type)

                                # Get original image size
                                $ orig_width, orig_height = renpy.image_size(equipment_img)

                                # Calculate proportional width
                                $ new_width = int(orig_width * (items_scale / float(orig_height)))

                                # Scale the image
                                $ equipment_scaled = im.Scale(equipment_img, new_width, items_scale)

                                $ button_action = Show("equipment_detail_screen", None, "e", equipment)
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 20
                                    vbox:
                                        xalign 0.5
                                        xminimum 700
                                        xmaximum 700
                                        vbox:
                                            xalign 0.5
                                            button:
                                                action button_action
                                                style "option_button_online_shop"
                                                xpadding 4
                                                ypadding 4
                                                frame:                                            
                                                    background my_color
                                                    xalign 0.5 
                                                    add im.Composite(
                                                        (items_scale, items_scale),
                                                        (0, 0), empty_scaled,
                                                        ((items_scale - new_width) // 2, 0), equipment_scaled   
                                                    )

                                    text str(equipment.name) xalign 0.5 color online_shop_color

                                    text str(equipment.price) + " $" xalign 0.5 color online_shop_color

                                    $ online_shop_action = Function(notify_user_money_is_not_enough, equipment.name)
                                    if money >= equipment.price:
                                        $ online_shop_action = Function(buy_new_equipment, equipment)

                                    if equipment.stillAvailable:
                                        button:
                                            style "option_button_online_shop"
                                            xfill True
                                            xmaximum 500
                                            xalign 0.5
                                            frame:
                                                xfill True
                                                background "#444"
                                                padding (10, 10)
                                                vbox:
                                                    spacing 5
                                                    xalign 0.5
                                                    text "Buy" size 24 color "#fff" xalign 0.5
                                            action online_shop_action
                                    
                hbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.5
                    $ text_style_S = "rarity_navegation_text_online_shop"
                    $ text_style_A = "rarity_navegation_text_online_shop"
                    $ text_style_B = "rarity_navegation_text_online_shop"
                    $ text_style_C = "rarity_navegation_text_online_shop"
                    $ text_style_D = "rarity_navegation_text_online_shop"
                    $ text_style_E = "rarity_navegation_text_online_shop"
                    
                    if rarity_selected == "S": 
                        $ text_style_S = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "A": 
                        $ text_style_A = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "B": 
                        $ text_style_B = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "C": 
                        $ text_style_C = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "D": 
                        $ text_style_D = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "E": 
                        $ text_style_E = "rarity_navegation_text_online_shop_active"
                    textbutton "S" action SetScreenVariable("rarity_selected", "S") yalign 0.9 xalign 0.5 text_style text_style_S
                    text "|"
                    textbutton "A" action SetScreenVariable("rarity_selected", "A") yalign 0.9 xalign 0.5 text_style text_style_A
                    text "|"
                    textbutton "B" action SetScreenVariable("rarity_selected", "B") yalign 0.9 xalign 0.5 text_style text_style_B
                    text "|"
                    textbutton "C" action SetScreenVariable("rarity_selected", "C") yalign 0.9 xalign 0.5 text_style text_style_C
                    text "|"
                    textbutton "D" action SetScreenVariable("rarity_selected", "D") yalign 0.9 xalign 0.5 text_style text_style_D
                    text "|"
                    textbutton "E" action SetScreenVariable("rarity_selected", "E") yalign 0.9 xalign 0.5 text_style text_style_E
                textbutton "Back" action [SetScreenVariable("online_shop_show", "main_menu"), SetScreenVariable("rarity_selected", "S")] yalign 0.9 xalign 0.5 text_style text_style_back_button

            if online_shop_show == "show_weapons":

                hbox:
                    spacing 50
                    xalign 0.5
                    yalign 0.5
                    for rarity, weapons in online_shop_variable.selling_weapons_list.items():
                        if rarity == rarity_selected:
                            for weapon in weapons:
                                $ my_color = EClassColor
                                $ rarity = weapon.rarity
                                if weapon.rarity == "D":
                                    $ my_color = DClassColor
                                if weapon.rarity == "C":
                                    $ my_color = CClassColor
                                if weapon.rarity == "B":
                                    $ my_color = BClassColor
                                if weapon.rarity == "A":
                                    $ my_color = AClassColor
                                if weapon.rarity == "S":
                                    $ my_color = SClassColor
                                
                                $ weapon_img = "images/weapons/{}.png".format(weapon.type)

                                # Get original image size
                                $ orig_width, orig_height = renpy.image_size(weapon_img)

                                # Calculate proportional width
                                $ new_width = int(orig_width * (items_scale / float(orig_height)))

                                # Scale the image
                                $ weapon_scaled = im.Scale(weapon_img, new_width, items_scale)

                                $ button_action = Show("equipment_detail_screen", None, "w", weapon)
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 20
                                    vbox:
                                        xalign 0.5
                                        xminimum 700
                                        xmaximum 700
                                        vbox:
                                            xalign 0.5
                                            button:
                                                action button_action
                                                style "option_button_online_shop"
                                                xpadding 4
                                                ypadding 4
                                                frame:                                            
                                                    background my_color
                                                    xalign 0.5 
                                                    add im.Composite(
                                                        (items_scale, items_scale),
                                                        (0, 0), empty_scaled,
                                                        ((items_scale - new_width) // 2, 0), weapon_scaled   
                                                    )

                                    text str(weapon.name) xalign 0.5 color online_shop_color

                                    text str(weapon.price) + " $" xalign 0.5 color online_shop_color

                                    $ online_shop_action = Function(notify_user_money_is_not_enough, weapon.name)
                                    if money >= weapon.price:
                                        $ online_shop_action = Function(buy_new_weapon, weapon)

                                    if weapon.stillAvailable:
                                        button:
                                            style "option_button_online_shop"
                                            xfill True
                                            xmaximum 500
                                            xalign 0.5
                                            frame:
                                                xfill True
                                                background "#444"
                                                padding (10, 10)
                                                vbox:
                                                    spacing 5
                                                    xalign 0.5
                                                    text "Buy" size 24 color "#fff" xalign 0.5
                                            action online_shop_action
                hbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.5
                    $ text_style_S = "rarity_navegation_text_online_shop"
                    $ text_style_A = "rarity_navegation_text_online_shop"
                    $ text_style_B = "rarity_navegation_text_online_shop"
                    $ text_style_C = "rarity_navegation_text_online_shop"
                    $ text_style_D = "rarity_navegation_text_online_shop"
                    $ text_style_E = "rarity_navegation_text_online_shop"
                    
                    if rarity_selected == "S": 
                        $ text_style_S = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "A": 
                        $ text_style_A = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "B": 
                        $ text_style_B = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "C": 
                        $ text_style_C = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "D": 
                        $ text_style_D = "rarity_navegation_text_online_shop_active"
                    elif rarity_selected == "E": 
                        $ text_style_E = "rarity_navegation_text_online_shop_active"
                    textbutton "S" action SetScreenVariable("rarity_selected", "S") yalign 0.9 xalign 0.5 text_style text_style_S
                    text "|"
                    textbutton "A" action SetScreenVariable("rarity_selected", "A") yalign 0.9 xalign 0.5 text_style text_style_A
                    text "|"
                    textbutton "B" action SetScreenVariable("rarity_selected", "B") yalign 0.9 xalign 0.5 text_style text_style_B
                    text "|"
                    textbutton "C" action SetScreenVariable("rarity_selected", "C") yalign 0.9 xalign 0.5 text_style text_style_C
                    text "|"
                    textbutton "D" action SetScreenVariable("rarity_selected", "D") yalign 0.9 xalign 0.5 text_style text_style_D
                    text "|"
                    textbutton "E" action SetScreenVariable("rarity_selected", "E") yalign 0.9 xalign 0.5 text_style text_style_E
                textbutton "Back" action [SetScreenVariable("online_shop_show", "main_menu"), SetScreenVariable("rarity_selected", "S")] yalign 0.9 xalign 0.5 text_style text_style_back_button

            if online_shop_show == "show_protectors":
                
                hbox:
                    spacing 50
                    xalign 0.5
                    yalign 0.5
                    for protector_to_sell in online_shop_variable.selling_protectors_list:

                        $ image_name = protector_to_sell.stage

                        # Path to the image
                        $ show_protectors_image = "images/protectors/{}/{}.png".format(protector_to_sell.name, image_name)

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(show_protectors_image)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (items_scale / float(orig_height)))

                        # Scale the image
                        $ show_protectors_scaled = im.Scale(show_protectors_image, new_width, items_scale)

                        $ button_action = Show("protector_detail_screen", my_protector=protector_to_sell)
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 20
                            vbox:
                                xalign 0.5
                                xminimum 700
                                xmaximum 700
                                vbox:
                                    xalign 0.5
                                    button:
                                        action button_action
                                        style "option_button_online_shop"
                                        xpadding 4
                                        ypadding 4
                                        frame:
                                            xalign 0.5 
                                            add im.Composite(
                                                (items_scale, items_scale),
                                                (0, 0), empty_scaled,
                                                ((items_scale - new_width) // 2, 0), show_protectors_scaled   
                                            )

                            text str(protector_to_sell.name) xalign 0.5 color online_shop_color

                            text str(protector_to_sell.price) + " $" xalign 0.5 color online_shop_color

                            $ online_shop_action = Function(notify_user_money_is_not_enough, protector_to_sell.name)
                            if money >= protector_to_sell.price:
                                $ online_shop_action = Function(buy_new_protector, protector_to_sell)

                            if protector_to_sell.stillAvailable:
                                button:
                                    style "option_button_online_shop"
                                    xfill True
                                    xmaximum 500
                                    xalign 0.5
                                    frame:
                                        xfill True
                                        background "#444"
                                        padding (10, 10)
                                        vbox:
                                            spacing 5
                                            xalign 0.5
                                            text "Buy" size 24 color "#fff" xalign 0.5
                                    action online_shop_action
                textbutton "Back" action [SetScreenVariable("online_shop_show", "main_menu"), SetScreenVariable("rarity_selected", "S")] yalign 0.9 xalign 0.5 text_style text_style_back_button
                    
        hbox:
            spacing 20
            xalign 0.5
            yalign 0.99
            textbutton "Return" action Return() xalign 0.5 text_style text_style_back_button


screen boss_expedition(bossExpedition, fight):
    $ my_protector = fight.protector
    $ enemy = fight.enemy
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 650

        $ buttons_background = im.Scale("images/background_item.png", scale, scale)

        fixed:
            xfill True
            yfill True

            vbox:
                yalign 0.1
                xalign 0.5
                text "[bossExpedition.title]" size 50 color "#FFF" xalign 0.5
                text "[my_protector.get_attack_speed()]"
                text "[enemy.get_attack_speed()]"
                text "[fight.protector_time_until_atack]"
                text "[fight.enemy_time_until_atack]"
            fixed:
                yalign 1.0
                xalign 0.0
                spacing 50
                ymaximum 850
                
                vbox:
                    yalign 1.0
                    xalign 0.0
                    spacing 5
                    # Adding protector image
                    python:
                        image_name = my_protector.stage
                        if my_protector.stage >= 5:
                            image_name = str(my_protector.stage) + "_" + str(my_protector.chosen_evolution)
                        image_path = getImage(str(get_folder_from_map(my_protector.name)) + '/' + str(image_name))
                        if image_path:
                            ui.at(fit_to_screen_height)
                            ui.add(image_path)
            fixed:
                yalign 0.0
                xalign 0.0
                spacing 5
                ymaximum 200
                
                vbox:
                    yalign 1.0
                    xalign 0.0
                    spacing 5
                    bar value my_protector.hp range my_protector.get_health_points() style "hp_bar"
                    text "[int(my_protector.hp)] / [my_protector.get_health_points()]" size 20 color "#DDD"
                    bar value my_protector.get_mana_points() range my_protector.get_mana_points() style "mana_bar"
                    text "[my_protector.get_mana_points()] / [my_protector.get_mana_points()]" size 20 color "#DDD"
            vbox:
                yalign 1.0
                xalign 1.0
                spacing 50
                ymaximum 850
                vbox:
                    yalign 1.0
                    xalign 1.0
                    spacing 5
                    # Adding protector image
                    python:
                        image_path = getImage("images/expedition_bosses/" + str(enemy.name) + '/1')
                        if image_path:
                            ui.at(fit_to_screen_height)
                            ui.add(image_path)
            fixed:
                yalign 0.0
                xalign 1.0
                spacing 50
                ymaximum 200
                
                vbox:
                    yalign 1.0
                    xalign 1.0
                    spacing 5
                    bar value enemy.hp range enemy.get_health_points() style "hp_bar"
                    text "[int(enemy.hp)] / [enemy.get_health_points()]" size 20 color "#DDD"
                    bar value enemy.get_mana_points() range enemy.get_mana_points() style "mana_bar"
                    text "[enemy.get_mana_points()] / [enemy.get_mana_points()]" size 20 color "#DDD"
            vbox:
                yalign 0.5
                xalign 0.5
                spacing 50
                
            if fight.your_turn == True:
                # Top row: two buttons
                hbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    button:
                        frame:
                            style "square_button"
                            padding (10, 10)
                            vbox:
                                xalign 0.5  # horizontal center
                                yalign 0.5  # vertical center
                                spacing 5
                                text "Attack"
                        action Function(fight.protector_attack_enemy)
                    
                    button:
                        frame:
                            style "square_button"
                            padding (10, 10)
                            vbox:
                                xalign 0.5  # horizontal center
                                yalign 0.5  # vertical center
                                spacing 5
                                text "Defend"
                        action Function(fight.protector_defend_enemy) 
                    
                    button:
                        frame:
                            style "square_button"
                            padding (10, 10)
                            vbox:
                                xalign 0.5  # horizontal center
                                yalign 0.5  # vertical center
                                spacing 5
                                text "Flee"
                        action [Show("boss_expedition_results", None, bossExpedition, bossExpeditionFledResult), Hide("boss_expedition")]
            if fight.your_turn == False:
                $ continue_action = Function(fight.continue_fight)
                if fight.battle_message == fight_victory_message:
                    $ continue_action = [Show("boss_expedition_results", None, bossExpedition, bossExpeditionVictoryResult), Hide("boss_expedition")]
                elif fight.battle_message == fight_defeat_message:
                    $ continue_action = [Show("boss_expedition_results", None, bossExpedition, bossExpeditionDefeatResult), Hide("boss_expedition")]
                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    textbutton fight.battle_message text_style "message_boss_expedition_textbutton" action continue_action xalign 0.5


screen boss_expedition_results(bossExpedition, result):
    frame:
        modal True
        background Solid(black_color)
        xysize (config.screen_width, config.screen_height)
        $ scale = 650

        $ buttons_background = im.Scale("images/background_item.png", scale, scale)

        fixed:
            xfill True
            yfill True

            vbox:
                yalign 0.15
                xalign 0.5
                spacing 100
                text "[bossExpedition.title]" size 30 color "#FFF" xalign 0.5
                text "[result]" size 50 color "#FFF" xalign 0.5

            vbox:
                yalign 0.5
                xalign 0.5
                spacing 20
                $ expedition_stage_names = list(expedition_stages.keys())
                if result == bossExpeditionVictoryResult:
                    text "Victory! You crushed it! You are now the hero of [expedition_stage_names[int(bossExpedition.regionNumber - 1)]]!" size 20 color "#FFF" xalign 0.5
                    text "You have unlocked the next region: [expedition_stage_names[int(bossExpedition.regionNumber)]]" size 20 color "#FFF" xalign 0.5
                    text "Time to collect your rewards and get ready for the next challenge." size 20 color "#FFF" xalign 0.5
                elif result == bossExpeditionDefeatResult:
                    text "You were defeated by the [bossExpedition.title]!" size 25 color "#FFF" xalign 0.5
                    text "Don’t give up! Take on more missions, gain experience, level up, and come back stronger!" size 25 color "#FFF" xalign 0.5
                    text "You might also find better equipment in the shop." size 25 color "#FFF" xalign 0.5
                elif result == bossExpeditionFledResult:
                    text "You fled the battle agaisnt the [bossExpedition.title]!" size 25 color "#FFF" xalign 0.5
                    text "Don’t give up! Take on more missions, gain experience, level up, and come back stronger!" size 25 color "#FFF" xalign 0.5
                    text "You might also find better equipment in the shop." size 25 color "#FFF" xalign 0.5
                
                
            vbox:
                yalign 0.9
                xalign 0.5
                button:
                        frame:
                            style "rectangle_button"
                            padding (10, 10)
                            vbox:
                                xalign 0.5  # horizontal center
                                yalign 0.5  # vertical center
                                spacing 5
                                text "Continue"
                        action [Function(bossExpedition.finishBossExpedition, result), Hide("boss_expedition_results"), Jump("resting_area")]