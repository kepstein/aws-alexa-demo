from alexa.ask.utils import VoiceHandler, ResponseBuilder as r
from meetup_rsvps import PickAWinner

"""
In this file we specify default event handlers which are then populated into the handler map using metaprogramming
Copyright Anjishnu Kumar 2015

Each VoiceHandler function receives a ResponseBuilder object as input and outputs a Response object
A response object is defined as the output of ResponseBuilder.create_response()
"""


def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request """
    print("[debug] Didn't match any intents, therefore we invoked the default handler")
    return r.create_response(message="Just ask")


@VoiceHandler(request_type="LaunchRequest")
def launch_request_handler(request):
    """
    Annoatate functions with @VoiceHandler so that they can be automatically mapped
    to request types.
    Use the 'request_type' field to map them to non-intent requests
    """
    print("[debug] Request type was LaunchRequest")
    return r.create_response(message="Hello Welcome to My Recipes!")


@VoiceHandler(request_type="SessionEndedRequest")
def session_ended_request_handler(request):
    print("[debug] Request type was SessionEndedRequest")
    return r.create_response(message="Goodbye!")


@VoiceHandler(intent='PickWinnerIntent')
def get_winner_intent_handler(request):
    winner =PickAWinner()
    print("[debug] Called the PickWinnerIntent Intent")
    card = r.create_card(title="Picking Winners!",
                         subtitle=None,
                         content="The winner is " + winner)

    return r.create_response(message="The winner is " + winner,
                             end_session=True,
                             card_obj=card)


@VoiceHandler(intent='AMAZON.HelpIntent')
def get_help_intent_handler(request):
    """
    Use the 'intent' field in the VoiceHandler to map to the respective intent.
    You can insert arbitrary business logic code here
    """

    # Get variables like userId, slots, intent name etc from the 'Request' object
    # ingredient = request.get_slot_value("Ingredient")
    # ingredient = ingredient if ingredient else ""

    #Use ResponseBuilder object to build responses and UI cards
    print("[debug] Called the HelpIntent Intent")
    card = r.create_card(title="Handy Helper",
                         subtitle=None,
                         content="Ok, you need some help")

    return r.create_response(message="Ok, you need some help",
                             end_session=True,
                             card_obj=card)


@VoiceHandler(intent='AMAZON.StopIntent')
def get_stop_intent(request):
    print("[debug] AMAZON.StopIntent was called")
    session_ended_request_handler(request)
    pass

@VoiceHandler(intent='WelcomeIntent')
def get_welcome_intent_handler(request):
    response_text = "Welcome to the Los Angeles A.W.S Meetup. \
    This month we're talking about A.W.S Lambda, and what better way to demo Lambda than to \
    have Alexa call Lambda Functions. This demo function will call the Meetup A.P.I and check \
    to see who R S V P'd for this event and randomly pick one of those members to win an Amazon Echo."
    return r.create_response(message=response_text,
                             end_session=True)
