from .interpreter import *
#from .world import World

class Game:
    """
    Runs an interactive fiction game. This implementation uses the
    terminal window for interaction. This is the class you would
    need to override to use a more graphical game text window.
    """

    def __init__(self, world, interpreter: InterpreterContext = None):
        self.world = world
        self.interpreter = interpreter or InterpreterContext()
    

    def on_command(self, command):
        """
        Pass a received command to the interpreter, then to the be processed by 
        the systems in the world.
        """
        self.world.process_intent(self.interpreter.interpret(command), self)
    

    def output(self, text):
        """
        Called when a system tries to output game text. Override to redirect text 
        to somewhere other than stdout.
        """
        print(text)
    

    def ask(self, question):
        """
        Called when a system needs more information from the user. Override to use 
        something other than stdout & stdin.
        """
        print(question)
        return input('---> ')
    

    def on_frame(self):
        """
        Called once per "frame" of the game to check for a new command from the
        user. A frame is here defined as one iteration of the main loop, even 
        though interactive fiction obviously doesn't have true frames like a 
        graphical game. This will typically involve receiving text from the user 
        and displaying a response.

        This method is intended to get a command from the user and pass it to
        on_command. If you override this method, you must make sure to call 
        on_command here if and when you receive a command.
        """
        self.on_command(input('-> '))
    

    def start(self):
        """
        Start the game using a built-in main loop. If you are using your own main
        loop, or an event-based system that does not have a main loop, you will
        probably want to just manually call on_frame and on_quit yourself.
        """
        self.running = True
        try:
            while self.running:
                self.on_frame()
        except QuitGame:
            self.running = False
        self.on_quit()
    

    def quit(self):
        """
        Stop the built-in main loop
        """
        self.running = False
    

    def on_quit(self):
        """
        Called when the game exits. Override this to same game data, print a goodye 
        message, etc...
        """
        print("Goodbye!")


class QuitGame(Exception):
    """
    Raise this to signal it is time to end the game
    """
    pass


