def similarity(a,b):
    if len(a) != len(b):
        raise
    if len(a) == 0:
        raise
    return [a[i]==b[i] for i in range(len(a))].count(True)

def similarity_search(words, a, s):
    return [word for word in words if similarity(a, word) == s]

def main():
    print "Welcome to HACK-BOY 9001"
    print "List of Commands:"
    print "  PLAY _        : Play a game with me! Optionally give a length of word to play!"
    print "                  (Further instructions are given when playing)"
    print "  CLEAR         : Clear a hack session"
    print "  ADD _ [_ ...] : Add one or more words to a hack session."
    print "  TRY word sim  : Record a hacking attempt. word = word you guessed."
    print "                  sim = similarity reported by the terminal."
    print "  DUD word      : Strike a word out of the hacking session"
    print
    print "One letter can be used in place of full command. You can use P, C, A, T, and D."

if __name__ == "__main__":
    main()
