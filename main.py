from pprint import pprint
from leap import Leap, ApiException
import os

leap = Leap(
    host="https://api.tryleap.ai",
    access_token=os.env.get('API_KEY'),
);


try:
    # Generate an Song
    generate_response = leap.music.generate(
        prompt="A photo of an astronaut riding a horse",  # required
        model_id="26a1a203-3a46-42cb-8cfa-f4de075907d8",  # required
        negative_prompt="",  # optional
        # steps=50,  # optional
        # width=1024,  # optional
        # height=1024,  # optional
        # number_of_images=1,  # optional
        # prompt_strength=7,  # optional
        # seed=4523184,  # optional
        # webhook_url="string_example",  # optional
    )
    pprint(generate_response.body)
    pprint(generate_response.body["id"])
    pprint(generate_response.body["created_at"])
    pprint(generate_response.body["prompt"])
    pprint(generate_response.body["negative_prompt"])
    pprint(generate_response.body["seed"])
    pprint(generate_response.body["width"])
    pprint(generate_response.body["height"])
    pprint(generate_response.body["prompt_strength"])
    pprint(generate_response.body["number_of_images"])
    pprint(generate_response.body["state"])
    pprint(generate_response.body["status"])
    pprint(generate_response.body["steps"])
    pprint(generate_response.body["images"])
    pprint(generate_response.body["model_id"])
    pprint(generate_response.body["upscaling_option"])
    pprint(generate_response.headers)
    pprint(generate_response.status)
    pprint(generate_response.round_trip_time)
    
except ApiException as e:
    print("Exception when calling ImagesApi.generate: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)