def welcome(fx):
  def mfx():
    print("Good Morning")
    fx()
  return mfx

@welcome
def print():
    print("hello")
print()
