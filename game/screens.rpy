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
    xalign 0.99999
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

screen my_weapons_screen():
    frame:
        modal True
        background Solid("#000000ff")
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
        background Solid("#000000ff")
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

                                            $ equipment_img = "images/equipment/{}_{}.png".format(equipment.class_name, equipment.type)

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
        background Solid("#000000ff")
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
        background Solid("#000000ea")
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
        background Solid("#000000ff")
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
                    $ e_or_w_image = "images/equipment/{}_{}.png".format(equipment_or_weapon.class_name, equipment_or_weapon.type)

                # Get original image size
                $ orig_width, orig_height = renpy.image_size(e_or_w_image)

                # Calculate proportional width
                $ new_width = int(orig_width * (scale / float(orig_height)))

                # Scale the image
                $ e_or_w_scaled = im.Scale(e_or_w_image, new_width, scale)

                frame:
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
                            text "Improved attribute 1:" size 22 color "#EEE"
                            text "Improved attribute 2:" size 22 color "#EEE"

                        text "Rarity:" size 22 color "#EEE"
                        
                    vbox:
                        xminimum 300
                        xalign 0.5
                        if protector is not None:
                            text protector.name size 22 color "#EEE" xalign 0.99999999999
                        text "[str(equipment_or_weapon.type)]" size 22 color "#EEE" xalign 0.99999999999
                        text "[str(equipment_or_weapon.class_name)]" size 22 color "#EEE" xalign 0.99999999999
                        if weaponOrEquipment_type == "w":
                            text "[str(equipment_or_weapon.base_damage)]" size 22 color "#EEE" xalign 0.99999999999
                            text "[str(equipment_or_weapon.range)]" size 22 color "#EEE" xalign 0.99999999999
                        elif weaponOrEquipment_type == "e":
                            text "[str(equipment_or_weapon.base_defense)]" size 22 color "#EEE" xalign 0.99999999999
                            text "[str(stats_increment_map[equipment_or_weapon.class_name]['prio1'])] (x[str(equipment_or_weapon.prio1 + 1)])" size 22 color "#EEE" xalign 0.99999999999
                            text "[str(stats_increment_map[equipment_or_weapon.class_name]['prio2'])] (x[str(equipment_or_weapon.prio2 + 1)])" size 22 color "#EEE" xalign 0.99999999999
                        
                        text "[str(equipment_or_weapon.rarity)]" size 22 color "#EEE" xalign 0.99999999999
                            
screen protector_evolution_choosing_screen(my_protector):
    frame:
        modal True
        background Solid("#000000ff")
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
        background Solid("#000000ff")
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
                    $ spe_text = str(current_stats['Speed']) + " → " + str(evolution_stats['Speed']) + " (+" + str(percentage_change) + "%)"
                elif "Speed" in decrease_array:
                    $ percentage_change = decreasing_percentage * decrease_array.count("Speed")
                    $ spe_t_color = "#F44336"
                    $ spe_text = str(current_stats['Speed']) + " → " + str(evolution_stats['Speed']) + " (-" + str(percentage_change) + "%)"
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

                        
screen protector_detail_screen(my_protector):
    $ scale = 125
    $ action_button = None
    frame:
        modal True
        background Solid("#000000ff")
        xysize (config.screen_width, config.screen_height)

        fixed:
            xfill True
            yfill True

            # Image - mid right, just below the name
            python:
                image_name = my_protector.stage
                if my_protector.stage >= 5:
                    image_name = str(my_protector.stage) + "_" + str(my_protector.chosen_evolution)
                image_path = getImage(str(get_folder_from_map(my_protector.name)) + '/' + str(image_name))
                if image_path:
                    ui.at(center)
                    ui.at(fit_to_screen_height)
                    ui.add(image_path)

            # Close button - top right
            textbutton "Back" action Hide("protector_detail_screen"):
                text_style "hover_white"
                xalign 1.0
                yalign 0.0
                padding (10, 5)
            
            vbox:
                yalign 0.05
                xalign 0.5
                
                if my_protector.chosen_evolution != 0:
                    $ evolution_name = my_protector.basePoints.evolution_name_1
                    if my_protector.chosen_evolution == 2:
                        $ evolution_name = my_protector.basePoints.evolution_name_2
                    text "[evolution_name] ([my_protector.status])" size 50 color "#FFF" xalign 0.5
                    
                else:
                    text "[my_protector.name] ([my_protector.status])" size 50 color "#FFF" xalign 0.5

            hbox:
                xalign 0.5
                yalign 0.95
                spacing 20
                text "Level: [my_protector.level]" size 25 color "#DDD"
                text "Stage: [my_protector.stage]" size 25 color "#DDD"
                    
            # Text block - vertically centered on left side
            vbox:
                spacing 20
                xalign 0.0000000000001
                yalign 0.5
                xmaximum 500
                xfill True
                hbox:
                    xalign 0.5
                    spacing 20
                    $ empty_scaled = im.Scale("images/background_item.png", scale, scale)
                    if my_protector.equipedWeapon == None:
                        $ weapon_img = "images/weapons/default_weapon.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(weapon_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ weapon_scaled = im.Scale(weapon_img, new_width, scale)

                        if my_protector.status == "Available" and my_protector.basePoints.can_it_use_weapons == True:
                            $ action_button = Function(show_weapons, my_protector)
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_scaled,
                                    ((scale - new_width) // 2, 0), weapon_scaled   
                                )
                    else:
                        $ weapon_img = "images/weapons/{}.png".format(my_protector.equipedWeapon.type)
                        $ background_color_style = EClassColor
                        if my_protector.equipedWeapon.rarity == "D":
                            $ background_color_style = DClassColor
                        if my_protector.equipedWeapon.rarity == "C":
                            $ background_color_style = CClassColor
                        if my_protector.equipedWeapon.rarity == "B":
                            $ background_color_style = BClassColor
                        if my_protector.equipedWeapon.rarity == "A":
                            $ background_color_style = AClassColor
                        if my_protector.equipedWeapon.rarity == "S":
                            $ background_color_style = SClassColor
                            
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(weapon_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ weapon_scaled = im.Scale(weapon_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Function(my_protector.unequip_weapon)
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_scaled,
                                    ((scale - new_width) // 2, 0), weapon_scaled   
                                )


                    
                    $ helmet_img = "images/equipment/no_helmet.png"
                    $ empty_helmet_scaled = im.Scale("images/background_item.png", scale, scale)
                    
                    $ body_img = "images/equipment/no_body.png"
                    $ empty_body_scaled = im.Scale("images/background_item.png", scale, scale)
                    
                    $ pants_img = "images/equipment/no_pants.png"
                    $ empty_pants_scaled = im.Scale("images/background_item.png", scale, scale)
                    
                    $ boots_img = "images/equipment/no_boots.png"
                    $ empty_boots_scaled = im.Scale("images/background_item.png", scale, scale)
                        

                    if my_protector.equipedHelmet == None:
                        $ helmet_img = "images/equipment/no_helmet.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(helmet_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ helmet_scaled = im.Scale(helmet_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Function(show_equipments, my_protector, "helmet")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_scaled,
                                    ((scale - new_width) // 2, 0), helmet_scaled
                                )
                    else:
                        $ helmet_img = "images/equipment/{}_{}.png".format(my_protector.equipedHelmet.class_name, my_protector.equipedHelmet.type)
                        $ helmet_scaled = im.Scale(helmet_img, 200, 200)
                        $ background_color_style = EClassColor
                        if my_protector.equipedHelmet.rarity == "D":
                            $ background_color_style = DClassColor
                        elif my_protector.equipedHelmet.rarity == "C":
                            $ background_color_style = CClassColor
                        elif my_protector.equipedHelmet.rarity == "B":
                            $ background_color_style = BClassColor
                        elif my_protector.equipedHelmet.rarity == "A":
                            $ background_color_style = AClassColor
                        elif my_protector.equipedHelmet.rarity == "S":
                            $ background_color_style = SClassColor
                        
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(helmet_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ helmet_scaled = im.Scale(helmet_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Function(my_protector.unequip_equipment, "helmet")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_scaled,
                                    ((scale - new_width) // 2, 0), helmet_scaled
                                )
                    if my_protector.equipedBodyArmor == None:
                        $ body_img = "images/equipment/no_body.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(body_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ body_scaled = im.Scale(body_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Function(show_equipments, my_protector, "body")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_body_scaled,
                                    ((scale - new_width) // 2, 0), body_scaled
                                )
                    else:
                        $ body_img = "images/equipment/{}_{}.png".format(my_protector.equipedBodyArmor.class_name, my_protector.equipedBodyArmor.type)
                        $ body_scaled = im.Scale(body_img, 200, 200)
                        $ background_color_style = EClassColor
                        if my_protector.equipedBodyArmor.rarity == "D":
                            $ background_color_style = DClassColor
                        if my_protector.equipedBodyArmor.rarity == "C":
                            $ background_color_style = CClassColor
                        if my_protector.equipedBodyArmor.rarity == "B":
                            $ background_color_style = BClassColor
                        if my_protector.equipedBodyArmor.rarity == "A":
                            $ background_color_style = AClassColor
                        if my_protector.equipedBodyArmor.rarity == "S":
                            $ background_color_style = SClassColor
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(body_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ body_scaled = im.Scale(body_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Function(my_protector.unequip_equipment, "body")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_body_scaled,
                                    ((scale - new_width) // 2, 0), body_scaled
                                )
                
                hbox:
                    xalign 0.5
                    spacing 20
                    if my_protector.equipedPants == None:
                        $ pants_img = "images/equipment/no_pants.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(pants_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ pants_scaled = im.Scale(pants_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Function(show_equipments, my_protector, "pants")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_pants_scaled,
                                    ((scale - new_width) // 2, 0), pants_scaled
                                )
                    else:
                        $ pants_img = "images/equipment/{}_{}.png".format(my_protector.equipedPants.class_name, my_protector.equipedPants.type)
                        $ pants_scaled = im.Scale(pants_img, 200, 200)
                        $ background_color_style = EClassColor
                        if my_protector.equipedPants.rarity == "D":
                            $ background_color_style = DClassColor
                        if my_protector.equipedPants.rarity == "C":
                            $ background_color_style = CClassColor
                        if my_protector.equipedPants.rarity == "B":
                            $ background_color_style = BClassColor
                        if my_protector.equipedPants.rarity == "A":
                            $ background_color_style = AClassColor
                        if my_protector.equipedPants.rarity == "S":
                            $ background_color_style = SClassColor
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(pants_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ pants_scaled = im.Scale(pants_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Function(my_protector.unequip_equipment, "pants")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_pants_scaled,
                                    ((scale - new_width) // 2, 0), pants_scaled
                                )

                    if my_protector.equipedBoots == None:
                        $ boots_img = "images/equipment/no_boots.png"

                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(boots_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ boots_scaled = im.Scale(boots_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Function(show_equipments, my_protector, "boots")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background "#ffffff"
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_boots_scaled,
                                    ((scale - new_width) // 2, 0), boots_scaled
                                )
                    else:
                        $ boots_img = "images/equipment/{}_{}.png".format(my_protector.equipedBoots.class_name, my_protector.equipedBoots.type)
                        $ boots_scaled = im.Scale(boots_img, 200, 200)
                        $ background_color_style = EClassColor
                        if my_protector.equipedBoots.rarity == "D":
                            $ background_color_style = DClassColor
                        if my_protector.equipedBoots.rarity == "C":
                            $ background_color_style = CClassColor
                        if my_protector.equipedBoots.rarity == "B":
                            $ background_color_style = BClassColor
                        if my_protector.equipedBoots.rarity == "A":
                            $ background_color_style = AClassColor
                        if my_protector.equipedBoots.rarity == "S":
                            $ background_color_style = SClassColor
                        # Get original image size
                        $ orig_width, orig_height = renpy.image_size(boots_img)

                        # Calculate proportional width
                        $ new_width = int(orig_width * (scale / float(orig_height)))

                        # Scale the image
                        $ boots_scaled = im.Scale(boots_img, new_width, scale)

                        if my_protector.status == "Available":
                            $ action_button = Function(my_protector.unequip_equipment, "boots")
                        else: 
                            $ action_button = Function(send_not_available_notification, my_protector, "Equipment not updatable")

                        button:
                            action action_button
                            xpadding 4
                            ypadding 4
                            background background_color_style
                            frame:
                                xalign 0.5 
                                add im.Composite(
                                    (scale, scale),
                                    (0, 0), empty_boots_scaled,
                                    ((scale - new_width) // 2, 0), boots_scaled
                                )
                
                # Text block - vertically centered on left side
                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    null height 10  # This adds 40 pixels of vertical space at the top
                    $ current_status = my_protector.get_current_stats()
                    hbox:
                        xalign 0.5
                        spacing 20
                        xfill True
                        vbox:
                            xalign 0.3
                            text "Strength:" size 22 color "#EEE" xalign 0.0000001
                            text "Dexterity:" size 22 color "#EEE" xalign 0.0000001
                            text "Constitution:" size 22 color "#EEE" xalign 0.0000001
                            text "Intelligence:" size 22 color "#EEE" xalign 0.0000001
                            text "Wisdom:" size 22 color "#EEE" xalign 0.0000001
                            text "Charisma:" size 22 color "#EEE" xalign 0.0000001
                            text "Speed:" size 22 color "#EEE" xalign 0.0000001
                            text "Luck:" size 22 color "#EEE" xalign 0.0000001
                        vbox:
                            xalign 0.7
                            text "[str(current_status['strength'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['dexterity'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['constitution'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['intelligence'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['wisdom'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['charisma'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['speed'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['luck'])]" size 22 color "#EEE" xalign 0.9999


            vbox:
                spacing 20
                xalign 0.99999999999
                yalign 0.5
                xmaximum 500
                xfill True
                vbox:
                    xalign 0.5
                    spacing 20
                    bar value my_protector.get_health_points() range my_protector.get_health_points() style "hp_bar"
                    text "[my_protector.get_health_points()] / [my_protector.get_health_points()]" size 20 color "#DDD"
                    bar value my_protector.get_mana_points() range my_protector.get_mana_points() style "mana_bar"
                    text "[my_protector.get_mana_points()] / [my_protector.get_mana_points()]" size 20 color "#DDD"
                    bar value my_protector.xp range my_protector.get_amount_of_xp_needed_for_leveling_up() style "xp_bar"
                    text "[my_protector.xp] / [my_protector.get_amount_of_xp_needed_for_leveling_up()]" size 20 color "#DDD"
                    null height 10  # This adds 40 pixels of vertical space at the top

                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    null height 10  # This adds 40 pixels of vertical space at the top
                    hbox:
                        xalign 0.5
                        spacing 20
                        xfill True
                        vbox:
                            xalign 0.3
                            text "Attack speed:" size 22 color "#EEE" xalign 0.0000001
                            text "Defense:" size 22 color "#EEE" xalign 0.0000001
                            text "Evasion:" size 22 color "#EEE" xalign 0.0000001
                            text "Morality:" size 22 color "#EEE" xalign 0.0000001
                            text "Cooldown reduction:" size 22 color "#EEE" xalign 0.0000001
                            text "Critical Damage:" size 22 color "#EEE" xalign 0.0000001
                            text "Critical chance:" size 22 color "#EEE" xalign 0.0000001
                        vbox:
                            xalign 0.7
                            text "[str(current_status['attack_speed'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['defense'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['evasion'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['morality'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(current_status['cooldown_reduction'])]" size 22 color "#EEE" xalign 0.9999
                            text "[str(round(current_status['critical_damage'] * 100, 2))]%" size 22 color "#EEE" xalign 0.9999
                            text "[str(round(current_status['critical_chance'] * 100, 2))]%" size 22 color "#EEE" xalign 0.9999
                vbox:
                    xalign 0.5
                    spacing 70
                    null height 10  # This adds 40 pixels of vertical space at the top
                    hbox:
                        xalign 0.5
                        spacing 25
                        vbox:
                            xalign 0.5
                            text "Real damage:" size 30 color "#EEE"
                        vbox:
                            xalign 0.5
                            text "[str(my_protector.get_damage_points())]" size 30 color "#EEE"

            if my_protector.readyForPromotion == True and my_protector.status == "Available":

                vbox:
                    xalign 0.5
                    yalign 0.8
                    text "Do you want to promote [my_protector.name]?" size 30 color "#FFF" xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing 150
                        vbox:
                            xalign 0.5
                            $ action_button = Function(my_protector.promote)
                            if my_protector.stage == 4:
                                $ action_button = Show("protector_evolution_choosing_screen", None, my_protector) 
                            textbutton "Yes" action action_button:
                                text_size 25
                                text_style "button_in_black_background"

                        vbox:
                            xalign 0.5
                            textbutton "No" action Hide("protector_detail_screen"):
                                text_size 25
                                text_style "button_in_black_background"

screen protector_selection(isThisMission):
    if isThisMission:
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
            if allMissions[0].status != "started":
                $ has_available = False
                for key, protector in my_protectors_map.items():
                    if protector.status == "Available":
                        $ has_available = True
                        textbutton protector.name + ' (' + str(protector.status) + ')' xalign 0.5 action [SetVariable("selected_protector", protector), Jump(where_to)]

                if not has_available:
                    text "No protectors are currently available." xalign 0.5
            else: 
                text "Training facility already occupied with: [my_protectors_map[allMissions[0].assignedProtectorName].name] " xalign 0.5
            textbutton "Back" action Return():
                text_style "hover_black"
                xalign 0.5

screen mission_screen(regionNumber):
    $ min_level = (regionNumber - 1) * 20
    $ max_level = regionNumber * 20
    default page = 0
    default page_size = 5
    default filtered_missions = [m for m in allMissions if min_level <= m.difficulty <= max_level and m.title != "Training"]
    default max_pages = max((len(filtered_missions) - 1) // page_size, 0)
    default mode = "list"
    default selected_mission = None
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
                            text "Missions" size 40
                        
                        vbox:
                            xalign 0.5
                            $ bossMission = next((m for m in bossMissions if m.regionNumber == regionNumber), None)
                            vbox:
                                xalign 0.5
                                bar value bossMission.successfulMinorMissions range bossMission.successfulMinorMissionsRequired:
                                    xmaximum 400
                                    ymaximum 30

                                vbox:
                                    xalign 0.5
                                    text "[bossMission.successfulMinorMissions] / [bossMission.successfulMinorMissionsRequired]" size 24

                    for i in range(page * page_size, min((page + 1) * page_size, len(filtered_missions))):
                        $ mission = filtered_missions[i]
                        button:
                            xfill True
                            frame:
                                xfill True
                                background "#444"
                                padding (10, 10)
                                vbox:
                                    spacing 5
                                    text "[mission.title] ([mission.mission_type])" size 24 color "#fff"
                                    text mission.description size 16 color "#ccc"
                                    text "Difficulty: [mission.difficulty]" size 14 color "#aaa"
                            action [SetScreenVariable("mode", "detail"), SetScreenVariable("selected_mission", mission)]

                    hbox:
                        spacing 20
                        xalign 0.5

                        if page > 0:
                            textbutton "Previous" action SetScreenVariable("page", page - 1)
                        else:
                            textbutton "Previous" action NullAction() sensitive False

                        if page < max_pages:
                            textbutton "Next" action SetScreenVariable("page", page + 1)
                        else:
                            textbutton "Next" action NullAction() sensitive False

                    textbutton "Return" action Return() xalign 0.5

            elif mode == "detail" and selected_mission is not None:
                vbox:
                    yalign 0.0
                    xalign 0.5
                    spacing 20
                    xsize 700
                    null height 40  # This adds 40 pixels of vertical space at the top
                    
                    vbox:
                        xalign 0.5
                        text "[selected_mission.title]" size 40 color "#000000"
                        
                        vbox:
                            xalign 0.5
                            spacing 20
                            text "([selected_mission.mission_type])" size 30 color "#000000"
                        
                            vbox:
                                xalign 0.5
                                text "Difficulty: [selected_mission.difficulty]" size 20 color "#5a5a5a"
                                
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top
                        
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    text selected_mission.description size 20 color "#5a5a5a"

                    $ neededDaysToFinish_day_name = "day"
                    $ disapearingInThisDays_day_name = "day"
                    if selected_mission.neededDaysToFinish > 1:
                        $ neededDaysToFinish_day_name = "days"
                    if selected_mission.disapearingInThisDays > 1:
                        $ disapearingInThisDays_day_name = "days"
                        
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top
                        
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top
                    hbox:
                        xsize 700
                        spacing 20

                        vbox:
                            xalign 0.0  # force to left
                            spacing 20

                            hbox:
                                text "Payment:" size 18 color "#5a5a5a"
                            hbox:
                                text "Time it takes to complete:" size 18 color "#5a5a5a"
                            if selected_mission.status != "started":
                                hbox:
                                    text "Will disappear in:" size 18 color "#5a5a5a"
                            if selected_mission.status == "assigned":
                                hbox:
                                    text "Assigned protector:" size 18 color "#5a5a5a"

                        vbox:
                            xalign 1.0  # force to right
                            spacing 20

                            hbox:
                                xalign 1.0  # force to right
                                text "[selected_mission.gold_received] $" size 18 color "#5a5a5a"
                            hbox:
                                xalign 1.0  # force to right
                                text "[selected_mission.neededDaysToFinish] [neededDaysToFinish_day_name]" size 18 color "#5a5a5a"
                            if selected_mission.status != "started":
                                hbox:
                                    xalign 1.0  # force to right
                                    text "[selected_mission.disapearingInThisDays] [disapearingInThisDays_day_name]" size 18 color "#5a5a5a"
                            if selected_mission.status == "assigned":
                                hbox:
                                    xalign 1.0  # force to right
                                    text "[selected_mission.assignedProtectorName]" size 18 color "#5a5a5a"
                
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    if selected_mission.status == "assigned":
                        $ success_rate = selected_mission.get_success_rate(my_protectors_map[selected_mission.assignedProtectorName])
                        if success_rate > 100:
                            $ success_rate = 100
                        vbox: 
                            xalign 0.5
                            spacing 10
                            bar value success_rate range 100 style "success_rate_bar"
                            text "Success rate: [success_rate] %" size 20 xalign 0.5
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top
                    # List of available protectors
                    $ available_protectors = [p for p in my_protectors_map.values() if p.status == "Available"]

                    if selected_mission.status != "started":                    
                        hbox:
                            xalign 0.5
                            spacing 10
                            for protector in available_protectors:
                                $ select_protector_button_style = "button_small_text"
                                if protector.name == selected_mission.assignedProtectorName:
                                    $ select_protector_button_style = "button_small_text_selected"
                                textbutton protector.name style str(select_protector_button_style) action Function(assign_protector, selected_mission.mission_id, protector.name)

                            
                            if len(available_protectors) == 0:
                                text "There are no available protectors." size 15 color "#5a5a5a" xmaximum 640

                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top

                    
                    vbox:
                        null width 40  # This adds 40 pixels of vertical space at the top
                    null ysize 1  # This adds 40 pixels of vertical space at the top
                    
                    hbox:
                        xalign 0.5
                        spacing 20
                        if selected_mission.status != "started" and selected_mission.assignedProtectorName != None:
                            textbutton "Start Mission" action Function(start_mission, selected_mission, protector.name, success_rate)
                        textbutton "Back" action SetScreenVariable("mode", "list")

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

            text "Select your weapon:" size 30

            # For each available weapon, create a button
            $ filtered_weapons = sorted(
                [weapon for weapon in myWeapons if weapon.type in protector.basePoints.usable_weapon_types],
                key=lambda weapon: (weapon.rarity, weapon.name.lower())
            )
            for weapon in filtered_weapons:
                textbutton "[weapon.name] ([weapon.rarity])":
                    action [Function(protector.equip_weapon, weapon.weapon_id), Hide("weapon_select")]
                    xminimum 200
                    ypadding 10

            textbutton "Cancel":
                action Hide("weapon_select")
                xminimum 200
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

            text "Select your equipment:" size 30

            # For each available weapon, create a button
            $ filtered_equipments = sorted(
                [equipment for equipment in myEquipments if equipment.type == equipment_type],
                key=lambda equipment: (equipment.rarity, equipment.name.lower())
            )
            for equipment in filtered_equipments:
                textbutton "[equipment.name] ([equipment.rarity])":
                    action [Function(protector.equip_equipment, equipment.equipment_id), Hide("equipment_select")]
                    xminimum 200
                    ypadding 10

            textbutton "Cancel":
                action Hide("equipment_select")
                xminimum 200
                ypadding 10


screen lucky_box_screen(box_type):
    frame:
        modal True
        background Solid("#000000ea")
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