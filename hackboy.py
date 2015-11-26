import cmd
import terminalsize
import textwrap

def similarity(a,b):
    if len(a) != len(b):
        raise Exception
    if len(a) == 0:
        raise Exception
    return [a[i]==b[i] for i in range(len(a))].count(True)

def similarity_search(words, a, s):
    return [word for word in words if similarity(a, word) == s]

class HackBoy9001Shell(cmd.Cmd):
    wordlist = []
    def printwords(self):
        """Nicely print words in columns, sensitive to console width!"""
        (console_width, console_height) = terminalsize.get_terminal_size()
        if len(self.wordlist) > 0:
            word_length = max([len(word) for word in self.wordlist]) + 1
            print word_length
            columns = console_width / word_length
            for index, word in enumerate(self.wordlist):
                if (index+1) % columns == 0:
                    print
                print word.ljust(word_length),
        print "\n%d words in list" % len(self.wordlist)

    def do_new(self, args):
        """n[ew]
           Begins a new hack session. Clears all existing words."""
        del self.wordlist[:]
        self.printwords()

    def do_add(self, args):
        """a[dd] WORD [...]
           One or more arguments required. Adds one or more words to a hack session."""
        if len(args) < 1:
            self.printwords()
            return
        args = args.split(' ')
        self.wordlist += [word.upper() for word in args if word not in self.wordlist]
        self.printwords()

    def do_try(self, args):
        """t[ry] WORD SIMILARITY
           Record a hacking attempt. Word list will automatically filter out non-candidates."""
        args = args.split(' ')
        if len(args) != 2:
            raise Exception
        if not isinstance(args[0], str):
            raise Exception
        try:
            args[1] = int(args[1])
        except ValueError:
            raise Exception
        self.wordlist = similarity_search(self.wordlist, args[0].upper(), args[1])
        self.printwords()

    def do_dud(self, args):
        """d[ud] WORD [...]
           Strike one or more words out of the hacking session. You probably won't need this."""
        args = args.split(' ')
        if len(args) < 1:
            raise
        self.wordlist = list(set(self.wordlist) - set(args))
        self.printwords()

    def do_list(self, args):
        """l[ist] | ls
           List the current possible passwords. 'ls' can also be used"""
        self.printwords()

    def do_sim(self, args):
        """s[im] WORD1 WORD2
           Check for similarity between two words."""
        args = args.upper().split(' ')
        if len(args) != 2:
            raise Exception
        if len(args[0]) != len(args[1]):
            raise Exception
        if len(args[0]) == 0:
            raise Exception
        print similarity(args[0], args[1])

    def do_clihelp(self, args):
        """[cli]help
           Command-Line Interface is not yet implemented.
           Print out full help for CLI mode. You damn geeks."""
        print "NotImplemented: CLI will be available at a later date."

    def do_apihelp(self, args):
        """[api]help
           Application Programming Interface is not yet implemented.
           Print out full help for API mode. You big goddamn geeks."""
        print "NotImplemented: API will be available at a later date."

    def do_quit(self, args):
        """quit
           Exit program"""
        raise SystemExit

    #StackOverflow 8813291
    def cmdloop(self):
        try:
            cmd.Cmd.cmdloop(self)
        except KeyboardInterrupt as e:
            raise SystemExit

    def do_about(self, args):
        '''about

           Tells you what this software is about'''
        (console_width, console_height) = terminalsize.get_terminal_size()
        for par in ['''\
            This tool, developed by NeCo Corporation, is designed to assist users with
            auditing RobCo TERMLINK security installations, which are notorious for
            flawed in-memory security.
            ''','','''
            Weaker passwords, usually 4 characters in length, are trivial and may not
            require much forethought. However, when encountered with strong security
            with no additional memory access attempts or filtering out improbable
            ciphers, it becomes more cumbersome for a security auditor or technician
            to service the system. This tool was therefore created.
            ''']:
            print textwrap.fill(textwrap.dedent(par), console_width)

    def do_license(self, args):
        '''license
           This software is provided to you under the C.I.T. License.

           Type "license" to see actual LEGAL JIBBER JABBERS.'''
        (console_width, console_height) = terminalsize.get_terminal_size()
        for par in ['''\
            This software is provided to you under the C.I.T. License.
            ''','''\
            (also known outside the Commonwealth as MIT License)
            ''','','''\
            Copyright (c) 2015 Chawanat Nakasan
            ''','','''\
            Permission is hereby granted, free of charge, to any person obtaining a copy
            of this software and associated documentation files (the "Software"), to deal
            in the Software without restriction, including without limitation the rights
            to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
            copies of the Software, and to permit persons to whom the Software is furnished
            to do so, subject to the following conditions:
            ''','','''\
            The above copyright notice and this permission notice shall be included in all
            copies or substantial portions of the software.
            ''','','''\
            THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
            IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
            FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
            AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGERS OR OTHER
            LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
            OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
            SOFTWARE.
            ''','','''\
            Actually I'm not that serious about license. Just wanted an excuse to say C.I.T. somewhere.
        ''','','''\
            Bethesda, Bethesda Softworks, Bethesda Game Studios, Fallout, PIP-BOY,
            Vault-Boy character, and Dogmeat are property of Bethesda Softworks.
            Other trademarks and intellectual properties are owned by their respective
            owners. This is a fan program and is not endorsed by any entities aforementioned.
            ''']:
            print textwrap.fill(textwrap.dedent(par), console_width)

    do_n = do_new
    do_a = do_add
    do_t = do_try
    do_d = do_dud
    do_l = do_list
    do_ls = do_list
    do_s = do_sim
    do_cli = do_clihelp
    do_api = do_apihelp
    do_q = do_quit

def main():
    print "Welcome to HACK-BOY 9001 (Interactive Mode)"
    print "If you're new here type \"help\" to get started."

    C = HackBoy9001Shell()
    C.prompt = '> '
    C.cmdloop()

if __name__ == "__main__":
    main()
