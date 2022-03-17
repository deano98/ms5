@dataclass
class ProductMetadata(object):
    '''
    Metadata for a Stripe product
    '''
    stripe_id: str
    name: str
    features: List[str]
    description: str = ''
    is_default: bool = False


BASIC = ProductMetadata(
    stripe_id="prod_LKKXDkSolThQ9k",
    name="Basic",
    description='Workout plan',
    is_default=False,
    features=[
        "Personalised Workout Plan",
    ],
)


PREMIUM = ProductMetadata(
    stripe_id="prod_LKc0tS0GYdmocz",
    name="Premium",
    description='Personalised nutrition plan as well as a workout plan',
    is_default=False,
    features=[
        "Personalised Workout Plan",
        "Personalised Nutriton Plan",
    ],
)