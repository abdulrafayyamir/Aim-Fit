import kivymd
from kivymd.app  import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton , MDRectangleFlatButton ,MDIconButton ,MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivymd.uix.list import MDList , TwoLineListItem ,OneLineListItem, TwoLineIconListItem ,IconLeftWidget , TwoLineAvatarIconListItem , ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import datetime

# Window.size = (360,640)

screenss = """
ScreenManager:
    Login:
    Account:
    Main:
    About:
    Bmi:
    Exercise:
    UnderWeightScreen:
    NormalWeightScreen:
    OverWeightScreen:
<Login>:
    name: "login"
    email: email
    password: password
    
    Image: 
        source : 'aimfit1.png'
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.7}
        size_hint : 0.5, 0.3
        
    MDTextField:
        id : email
        hint_text : "Enter Email"
        helper_text : "or click on Make New Account to create one"
        helper_text_mode : "on_focus"
        icon_right : "account-lock"
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {"center_x" : 0.5, "center_y" : 0.5 }
        size_hint_x : None
        width : 300
        
    MDTextField:
        id : password
        hint_text : "Enter Password"
        helper_text  : "or click on Make New Account to create one"
        helper_text_mode : "on_focus"
        icon_right : 'lock'
        icon_right_color : app.theme_cls.primary_color
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.4}
        size_hint_x : None
        width : 300
        
    MDRectangleFlatButton:
        text : '              Login              '
        pos_hint :{'center_x' : 0.5, 'center_y' : 0.25}
        on_press:
            root.manager.transition.direction = "up"
            root.loginBtn()    
                      
    MDRectangleFlatButton:
        text : 'Make New Account'
        pos_hint :{'center_x' : 0.5, 'center_y' : 0.15}
        on_press:
            root.manager.current = 'account'
            root.manager.transition.direction = "left"
    
        
<Account>:
    name : "account"
    
    namee: namee
    email: email
    password: passw
    
    Image: 
        source : 'aimfit1.png'
        pos_hint : {'center_x' : 0.5, 'center_y' : 0.7}
        size_hint : 0.5, 0.3
    MDTextField:
        id : namee
        hint_text : "Name"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.5 }
        size_hint_x : None
        width : 300    
    MDTextField:
        id : email
        hint_text : "Email"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.4 }
        size_hint_x : None
        width : 300    
    MDTextField:
        id : passw
        hint_text : "Password"
        pos_hint : {"center_x" : 0.5, "center_y" : 0.3 }
        size_hint_x : None
        width : 300
    MDRectangleFlatButton:
        text : 'Done'
        pos_hint: {'center_x': 0.5, 'center_y' : 0.2}
        on_press: 
            root.manager.transition.direction = "right"
            root.submit()
    MDRectangleFlatButton:
        text : 'Back'
        pos_hint: {'center_x': 0.5, 'center_y' : 0.1}
        on_press: 
            root.manager.transition.direction = "right"
            root.manager.current = 'login'        
     
<Main>:
    name : "aim"
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : "vertical"
                    MDToolbar:
                        title : "AimFit"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    Widget:
                Image:
                    source : 'aimfit2.png'
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.55}
                    size_hint : 1 , 0.7
                        
                MDRectangleFlatButton:
                    text : 'Lets get Started!'
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.2}
                    on_press : 
                        root.manager.current  = "bmi"
                        root.manager.transition.direction = "left"
                    
                MDBottomAppBar:
                    MDToolbar:
                        mode: "end"
                        type: "bottom"
                        icon: "home"
                        on_action_button: 
                            root.manager.current = 'aim'     

        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            IconLeftWidget:
                                icon : 'home'
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:     
                                root.manager.current = 'about'
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:     
                                    root.manager.current = 'about'
                                    root.manager.transition.direction = "up"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                    
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<About>:
    name : 'about'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : "vertical"
                    MDToolbar:
                        title : "AimFit"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                    Widget:
                Image:
                    source : 'aimfit1.png'
                    pos_hint : {'center_x' : 0.35 , 'center_y' : 0.8}
                    size_hint :  0.5 , 0.3 
                Image:
                    source : 'istlogo.png'
                    pos_hint : {'center_x' : 0.67 , 'center_y' : 0.8}
                    size_hint :  0.2 , 0.2    
                MDLabel:
                    text : "About Us"
                    font_style:'H3'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.6}
                    halign : 'center'
                    valign : 'middle'
                    theme_text_color : 'Custom'
                    text_color : 1,1,0,1
                MDLabel:
                    text : "A Object Oriented Programming project on Python that is bacially a fitness application that provides us the guidness towards our health and body state"
                    font_style:'Subtitle1'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.5}
                    halign : 'center'
                    valign : 'middle'
                MDLabel:
                    text : "Project by"
                    font_style:'H3'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.355}
                    halign : 'center'
                    valign : 'middle'
                    theme_text_color : 'Custom'
                    text_color : 1,1,0,1
                MDLabel:
                    text: " Muhammad Haseeb (210201057) , Riffah Eman (210201025) , Ibraheem Lugmani (210201044) , Abdul Rafay Amir (210201019) , Ahmad Bilal (210201096)"
                    font_style:'Subtitle1'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.2}
                    halign : 'center'
                    valign : 'middle'       
                MDBottomAppBar:
                    MDToolbar:
                        mode: "end"
                        type: "bottom"
                        icon: "home"
                        on_action_button: 
                            root.manager.current = 'aim'
                            root.manager.transition.direction = "up"      

        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            IconLeftWidget:
                                icon : 'face-profile'
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"         
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<Bmi>:
    name: 'bmi'
    
    weight: weight
    h: h
    ttttext : ttttext
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : "vertical"
                    MDToolbar:
                        title : "AimFit"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                    Widget:
                
                Image: 
                    source : 'aimfit1.png'
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.75}
                    size_hint : 0.5, 0.3 
                MDLabel:
                    text : "B.M.I Calculator"
                    font_style:'H3'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.55}
                    halign : 'center'
                    valign : 'middle'
                    theme_text_color : 'Custom'
                    text_color : 1,1,0,1        
                MDTextField:
                    id : weight
                    hint_text : "Enter Weight"
                    helper_text : "In Kilograms"
                    helper_text_mode : "on_focus"
                    pos_hint : {"center_x" : 0.5, "center_y" : 0.4 }
                    size_hint_x : None
                    width : 300
                    
                MDTextField:
                    id : h 
                    hint_text : "Enter Height"
                    helper_text : "In Meters(1 feet = 0.3 meters)"
                    helper_text_mode : "on_focus"
                    pos_hint : {"center_x" : 0.5, "center_y" : 0.3 }
                    size_hint_x : None
                    width : 300 
                
                MDRectangleFlatButton:
                    text : 'Calculate'
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.2}
                    on_press : 
                        root.calculate()
                        root.manager.transition.direction = "left"
                
                MDLabel:
                    id : ttttext 
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.145}
                    halign : 'center'
                    valign : 'middle'
             
                          
                MDBottomAppBar:
                    MDToolbar:
                        mode: "end"
                        type: "bottom"
                        icon: "home"
                        on_action_button: 
                            root.manager.current = 'aim'       

        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:
                                root.manager.current = 'about' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:
                                    root.manager.current = 'about' 
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                     
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<Exercise>:
    name : 'exercise'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation : "vertical"
                    MDToolbar:
                        title : "AimFit"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    Widget:
                Image:
                    source : 'aimfit1.png'
                    pos_hint : {'center_x' : 0.5, 'center_y' : 0.7}
                    size_hint : 0.5 , 0.3
                MDLabel:
                    text : "Select Category"
                    font_style:'H3'
                    pos_hint : {'center_x' : 0.5 ,'center_y' : 0.55}
                    halign : 'center'
                    valign : 'middle'
                    theme_text_color : 'Custom'
                    text_color : 1,1,0,1                    
                MDRectangleFlatButton:
                    text : '  Underweight  '
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.45}
                    on_press : 
                        root.manager.current  = "UnderWeight"
                        root.manager.transition.direction = "left"
                MDRectangleFlatButton:
                    text : 'Normalweight'
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.35}
                    on_press : 
                        root.manager.current  = "NormalWeight"
                        root.manager.transition.direction = "left"
                MDRectangleFlatButton:
                    text : '   Overweight   '
                    pos_hint : {'center_x' : 0.5 , 'center_y' : 0.25}
                    on_press : 
                        root.manager.current  = "OverWeight"
                        root.manager.transition.direction = "left"                             
                MDBottomAppBar:
                    MDToolbar:
                        mode: "end"
                        type: "bottom"
                        icon: "home"
                        on_action_button: 
                            root.manager.current = 'aim' 
        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:     
                                root.manager.current = 'about'
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:     
                                    root.manager.current = 'about'
                                    root.manager.transition.direction = "up"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            IconLeftWidget:
                                icon : 'weight-lifter'                                   
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<UnderWeightScreen>:
    name:'UnderWeight'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'  
                    MDToolbar:
                        title:'AimFit'
                        left_action_items:[["menu",lambda x:nav_drawer.set_state("open")]]
                    Widget:
                MDLabel:
                    text:'Exercises you need'
                    font_style:'H3'
                    theme_text_color:"Custom"
                    text_color:1,1,0,1
                    halign:'center'
                    valign:'middle'
                    height:self.texture_size[1] 
                    pos_hint : {'center_x':0.5 ,'center_y' : 0.85} 
                MDLabel:
                    text:'Push-ups'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.75}   
                MDLabel:
                    text:'Good old push-ups should be one of the first exercises that come to your mind when you think about weight gain. This is because push-ups help you build muscles in your chest and arms. When combined with the right protein and calorie diet, push-ups can turn into a lethal weapon in your weight gain arsenal. Push-ups are very efficient when they are done to the point of hypertrophy, i.e., muscle cell growth, and this is attained by pushing your body to the limit every time you do a push-up.'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.62}
                MDLabel:
                    text:'Deadlifts'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.48}
                MDLabel:
                    text:'Deadlifts are used by fitness trainers to help their students with weight loss and fat loss, but it is also a very potent tool for people to gain weight. Because of its ability to engage the maximum number of muscles in the body, it has a reputation for being one of the most credible exercises in helping you ensure your weight gain is distributed evenly among every part of your body.'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.35}
                MDLabel:
                    text:'Squats'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.25}
                MDLabel:
                    text:'Squats are powerful tools that people, especially underweight people, can use to build their butt muscles, leg muscles, and quads. If you are involved in a lot of fitness programs for fat loss and muscle gain, you must have come across this exercise many times.' 
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.16}
                MDBottomAppBar:
                    MDToolbar:    
                        mode:'end'   
                        type:'bottom' 
                        icon:'home'
                        on_action_button:    
                            root.manager.current='aim'
        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:
                                root.manager.current = 'about' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:
                                    root.manager.current = 'about' 
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                     
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<NormalWeightScreen>:
    name:'NormalWeight'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'  
                    MDToolbar:
                        title:'AimFit'
                        left_action_items:[["menu",lambda x:nav_drawer.set_state("open")]]
                    Widget:
                MDLabel:
                    text:'Exercises you need'
                    font_style:'H3'
                    theme_text_color:"Custom"
                    text_color:1,1,0,1
                    halign:'center'
                    valign:'middle'
                    height:self.texture_size[1] 
                    pos_hint : {'center_x':0.5 ,'center_y' : 0.85}    
                MDLabel:
                    text:'Dumbbell Rows'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.75}                    
                MDLabel:
                    text:'The dumbbell row, also known as the bent-over dumbbell row, is a compound back exercise. Perform dumbbell rows by hinging your hips with your back straight and lifting a pair of dumbbells with a neutral grip (palms facing each other). Like other rowing exercises, the dumbbell row uses a pulling movement pattern that activates multiple muscles in your upper back, shoulders, core, and arms.'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.62}
                MDLabel:
                    text:'Lunges'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.48}
                MDLabel:
                    text:'The lunge is a popular leg-strengthening exercise with a multitude of variations to add variety to your workout. In addition, varying your technique allows you to emphasize different muscles or parts of those muscles.This exercise is beneficial for injury prevention, as well as rehabilitation after injuries occur.'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.37}
                MDLabel:
                    text:'Burpees'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.27}
                MDLabel:
                    text:'Burpees are a challenging exercise that work many of the major muscle groups in your body. This versatile exercise may be worth the payoff, especially if you are looking for a way to build strength and endurance, while burning calories, and boosting your cardio fitness' 
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
        
                    pos_hint:{'center_x':0.5,'center_y':0.17} 
                MDBottomAppBar:
                    MDToolbar:  
                        mode:'end'
                        type:'bottom'
                        icon:'home'
                        on_action_button:  
                            root.manager.current='aim'                        

        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:
                                root.manager.current = 'about' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:
                                    root.manager.current = 'about' 
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                     
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"
<OverWeightScreen>:
    name:'OverWeight'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'  
                    MDToolbar:
                        title:'AimFit'
                        left_action_items:[["menu",lambda x:nav_drawer.set_state("open")]]
                    Widget:
                MDLabel:
                    text:'Exercises you need'
                    font_style:'H3'
                    theme_text_color:"Custom"
                    text_color:1,1,0,1
                    halign:'center'
                    valign:'middle'
                    height:self.texture_size[1] 
                    pos_hint : {'center_x':0.5 ,'center_y' : 0.85}    
                MDLabel:
                    text:'Walking'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.75}     
                MDLabel:
                    text:'It should come as no surprise that walking is one of the best exercises to focus on if you are looking to improve your fitness and lose weight. While the benefits of walking vary depending on sex and weight, walking 1 mile can burn approximately 100 calories.Even walking slowly may be able to help you get your heart rate up, and this is what is necessary for having a great cardio exercise'
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.62}
                MDLabel:
                    text:'Modified Push-Ups'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.48}
                MDLabel:
                    text:'It can be difficult to do push-ups if you are overweight, you can modify the exercise to make it easier. There are several ways you can do this if a standard push-up is too difficult.you can perform the exercise while standing up with your hands pushing against the wall instead of the floor. '
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.37}
                MDLabel:
                    text:'Side Leg Lifts'
                    font_style:'H4'
                    theme_text_color:'Custom'
                    halign:'center'
                    valign:'middle'
                    text_color:1,1,0,1
                    pos_hint:{'center_x':0.5,'center_y':0.27}
                MDLabel:
                    text:'Leg lifts are a great exercise for working out your lower body, and there are several types of leg lifts you can try. Side leg lifts, or side-lying hip abduction exercises, are one of the best types you may want to give a shot.Side leg lifts can be extremely beneficial for your lower body' 
                    padding_x:20
                    theme_text_color:'Custom'
                    text_color:1,1,1,1
                    halign:'center'
                    valign:'middle'
                    pos_hint:{'center_x':0.5,'center_y':0.17} 
                MDBottomAppBar:
                    MDToolbar:    
                        mode:'end'    
                        type:'bottom'
                        icon:'home'
                        on_action_button:
                            root.manager.current='aim'  
        MDNavigationDrawer:
            id : nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing : '8dp'
                padding : '8dp'
                Image:
                    source: 'aimfit2.png'
                    
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'AimFit'
                            on_press:     
                                root.manager.current = 'aim'
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'home'
                                on_press:     
                                    root.manager.current = 'aim'
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'About Us'
                            on_press:
                                root.manager.current = 'about' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'face-profile'
                                on_press:
                                    root.manager.current = 'about' 
                                    root.manager.transition.direction = "down"
                        OneLineIconListItem:
                            text: 'Exercise Plan'
                            on_press:
                                root.manager.current = 'exercise' 
                                root.manager.transition.direction = "up"
                            IconLeftWidget:
                                icon : 'weight-lifter'
                                on_press:     
                                    root.manager.current = 'exercise'
                                    root.manager.transition.direction = "up"                                    
                        OneLineIconListItem:
                            text: 'Logout'
                            on_press:
                                root.manager.current = 'login' 
                                root.manager.transition.direction = "down"
                            IconLeftWidget:
                                icon : 'logout'
                                on_press:     
                                    root.manager.current = 'login'
                                    root.manager.transition.direction = "down"                                              
"""

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

def invalid_form():
    pop  = MDDialog(title="Invalid Entry", text="Invaild Email or Password")
    pop.open()

def invalid_entry():
    pop1 = MDDialog(title = "Invalid entry",text = "You have entered invalid values")
    pop1.open()
    
class info():
    def bmi_1(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch1)
        self.p = MDDialog(title = "Serverly Underweight",text = "Your bmi is less then 16 this means that you are serverly underweight. Your diet plan is to Eat more of vegetables and fruits especially bananas, mangoes, watermelon, pomegranate, carrots, beans, broccoli, spinach, grapes, beetroot etc. Include good quality MUFA & PUFA rich oils.Ditch fast food for a while and drink plenty of water.",buttons=[e_button])
        self.p.open()
        
    def bmi_2(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch1)
        self.p = MDDialog(title = "Underweight",text = "Your bmi is between 16 and 18.5 this means that you are underweight. Your diet plan is to consume around 2200 calories a day.Try to increase the amount of food you eat 3 time a day. try to consume eggs, milk, almond, walnuts, fruit shakes, smoothie, fresh juices, vegitables curry and fruits, drick around 8 glass of water per day.",buttons=[e_button])
        self.p.open()

    def bmi_3(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch2)
        self.p = MDDialog(title = "Normal Healthy",text = "Your bmi is between 18.5 and 25 this means that you are in normal healthy condition. A healthy eating plan will lower your risk for heart disease and other health conditions. You Diet plan is to, Emphasizes vegetables, fruits, whole grains, and fat-free or low-fat dairy products. Includes lean meats, poultry, fish, beans, eggs, and nuts. Limits saturated and trans fats, sodium, and added sugars. Controls portion sizes.",buttons=[e_button])
        self.p.open()

    def bmi_4(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch3)
        self.p = MDDialog(title = "Overweight",text = "Your bmi is between 25 and 30 this means that you are Overweight. Your diet plan is to , Cut Down On Carbohydrates, Increase The Protein Intake, Keep Fat To A Minimum, Eat Less Energy - Dense Foods, Avoid “Feel Bad” Foods, Reduce The Intake Of Salt, Start With Soup, Get Enough B – Vitamins, Get Enough Vitamin D, Eat Vitamin C,  Get Enough Calcium, Eat Zinc and Consume Iodine.",buttons=[e_button])
        self.p.open()

    def bmi_5(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch3)
        self.p = MDDialog(title = "Moderatly Obese",text = "Your bmi is between 30 and 35 this means that you are moderatly obese. Your diet plan is to consume around 1600 calories a day. Try to eat oranges, apples, melons, guava, berries, and avoid banana, mango, litchi, grapes and other sugary fruits. Moderately include almonds, walnuts and flax seeds inure diet. Fish, chicken, egg whites can be consumed in moderation. Include healthy oils e.g. olive, mustard, sunflower oil. ",buttons=[e_button])
        self.p.open()

    def bmi_6(self):
        e_button = MDFlatButton(text='Exercise Plan' , on_release = self.switch3)
        self.p = MDDialog(title = "Serverly Obese",text = "Your bmi is greater than 35 this means that you are sererly obese. Your diet plan should include foods that have complex carbs. To get enough complex carbs, try to include brown rice, whole wheat bread, oatmeal, potatoes, sweet potatoes, and legumes. it should also include Protein-rich foods include chicken, beans, yogurt, eggs, fish, beef, lentils, chickpeas, beans, and so on.",buttons=[e_button])
        self.p.open()
    
    def switch1(self,obj):
        self.manager.current = "UnderWeight"
        self.p.dismiss()
        
    def switch2(self,obj):
        self.manager.current = "NormalWeight"
        self.p.dismiss()
        
    def switch3(self,obj):
        self.manager.current = "OverWeight"
        self.p.dismiss()               

class Login(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            self.reset()
            self.manager.current = "aim"
            
        else:
            invalid_form()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
    
class Account(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    
    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                self.manager.current= "login"
            else:
                invalid_form()
        else:
            invalid_form()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""
        
    
class Main(Screen):
    pass
class About(Screen):
    pass
class Bmi(Screen,info):
    weight = ObjectProperty(None)
    h = ObjectProperty(None)
    ttttext = ObjectProperty(None)
            
    def calculate(self):
        try:
            if self.weight.text != "" and self.h.text != "":
                val1 = float(self.weight.text)
                val2 = float(self.h.text)
                self.value = round(float(val1 / (val2)**2),1)
                self.reset()
            else:
                invalid_entry()    
        except:
            self.reset()
            invalid_entry()
            
        if self.value < 16:
            self.bmi_1()
        elif self.value >= 16 and self.value <= 18.5 :
            self.bmi_2()
        elif self.value > 18.5 and self.value <= 25 :
            self.bmi_3()       
        elif self.value > 25 and self.value <= 30 :
            self.bmi_4()
        elif self.value > 30 and self.value <= 35 :
            self.bmi_5()
        elif self.value > 35  :
            self.bmi_6()

        self.ttttext.text = "Your B.M.I is:  " + str(self.value)
                                              
    def reset(self):
        self.weight.text = ""
        self.h.text = ""

class Exercise(Screen):
    pass
class UnderWeightScreen(Screen):
    pass
class NormalWeightScreen(Screen):
    pass
class OverWeightScreen(Screen):
    pass

db = DataBase("users.txt")
sm = ScreenManager()
sm.add_widget(Login(name= "login"))
sm.add_widget(Account(name="account"))
sm.add_widget(Main(name="aim"))
sm.add_widget(About(name="about"))
sm.add_widget(Bmi(name="bmi"))
sm.add_widget(Exercise(name="exercise"))
class AimfitApp(MDApp):
        def build(self):
            self.theme_cls.primary_palette = "Yellow"
            self.theme_cls.primary_hue = "A700"
            self.theme_cls.theme_style = "Dark"
            screen = Builder.load_string(screenss)
            return screen      
App = AimfitApp()        
App.run()