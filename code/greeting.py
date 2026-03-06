def greeting(userNames: list[str]):
  if len(userNames) == 0:
    return
  for userName in userNames:
    print(f"Method: Life is short! {userName} use Python!")

if __name__ == "__main__":
  userNames: list[str] = ["Hasky", "Boild"]
  userName: str = "Beagle4ce"
  userNames += [userName]
  greeting(userNames)
