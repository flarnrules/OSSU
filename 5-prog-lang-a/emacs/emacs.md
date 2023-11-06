### A Markdown File
This is a markdown file.
I'm filling it with content via Emacs, which is not a code editor that I'm familiar with. That said, it seems like something that could be a lot of fun to edit with after learning how some of the commands work.

It's better than VIM for me right now because my VIM setup is busted AF.

It's probably worse than VS code for me right now because... VS code works right out of the box and doesn't have any weirdass keybindings. But this is pretty fun and interesting to work with.

One thing that's pretty dumb is that wordwrap is not by words, but by characters. So if a word isn't finished by the time you get to the end of a line, the word gets chopped up, making the content harder to read. I bet there's a setting to fix this, but It's probably time for bed soon so let's just move on.

To save and quit a buffer... we need to do this:

`C-x C-s`
And then just `C-x C-0` to close the window? Let's try.

Okay one mistake. It was `C-x 0` to close the window. Not bad tho!
Also, when I'm in Lisp interactive mode and the *scratch* buffer and run (show-buffers) it opens up a buffer to show me what buffers are available.
Getting to Lisp interactive mode can be through the command to open the directory: `C-x d` `enter`

NOPE. That shows the files in the directory I opened Emacs from. It doesn't show us all the buffers.

So the way we get the buffers to display is a simple command:
`C-x C-b`

So I think now is a good time to do the Emacs Tutorial again. Maybe this weekend?
Alright that's it.

### More Emacs Notes

Okay so now that I've spent some time learning Emacs, let's try and recap some of the key aspects of the keybindings.

**Windows**
To delete all windows but the active window, run `C-x 1`
To open a new buffer below, run `C-x 2`
To open a new buffer to the right, run `C-x 3`

**Main Stuff**
To save... I can't remember
To open the `*sml*` buffer, run `C-c C-s` -> I think this will only work if we have an `.sml` file open. From Emacs, to create a new file we can run:

This is where the *find* feature comes in!

Find is activated with `C-x C-f`
It then prompts us for what file we are looking for.
We can just **create** a file instead! Let's try.