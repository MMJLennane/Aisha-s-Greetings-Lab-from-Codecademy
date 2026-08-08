from contextlib import contextmanager


@contextmanager
def generic(card_type, sender_name, receiver):
	with open(card_type, "r") as template:
		with open(f"{sender_name}_generic.txt", "w") as card:
			card.write(f"Dear {receiver}\n")
			card.write(template.read())
			card.write(f"\nSincerely, {sender_name}")
			yield card


with generic("Thankyou_card.txt", "Mwenda", "Amanda") as card:
	print("Card Generated!")

with open("Mwenda_generic.txt", "r") as card:
	print(card.read())


class personalized:
	def __init__(self, sender, receiver):
		self.sender = sender
		self.receiver = receiver
		self.card = open(f"{sender}_personalized.txt", "w")

	def __enter__(self):
		self.card.write(f"Dear {self.receiver}\n")
		return self.card

	def __exit__(self, exc_type, exc_value, traceback):
		self.card.write(f"\nSincerely, {self.sender}")
		self.card.close()


with personalized("John", "Michael") as card:
	card.write(
		"I am so proud of you! Being your friend for all these years has been "
		"nothing but a blessing. I don't say it often but I just wanted to let "
		"you know that you inspire me and I love you! All the best. Always."
	)

with generic("happy_bday.txt", "Josiah", "Remy") as generic_card:
	with personalized("Josiah", "Esther") as personalized_card:
		personalized_card.write(
			"Happy Birthday!! I love you to the moon and back. Even though "
			"you're a pain sometimes, you're a pain I can't live without. I am "
			"incredibly proud of you and grateful to have you as a sister. "
			"Cheers to 25!! You're getting old!"
		)
