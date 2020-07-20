```
Computers store characters as numbers.
Every character used by a computer corresponds to a unique number, and vice versa.

ASCII (short for American Standard Code for Information Interchange) is the most widely
character ecnoding standard used.

The code provides space for 256 different characters, but we are interested only in the first 128
https://elcodigoascii.com.ar/

A classic form of ASCII code uses eight bits for each sign. Eight bits mean 256 different characters.
The first 128 are used for the standard Latin alphabet (both upper-case and lower-case characters).
Is it possible to push all the other national characters used around the world into the remaining 128 locations?
No. It isn't.

The word internationalization is commonly shortened to I18N.
Why? Look carefully - there is an I at the front of the word, next there are 18 different letters,
and an N at the end.

##### Code points and code pages
A code point is a number which makes a character. For example, 32 is a code point which makes a space in ASCII encoding. We can say that standard ASCII code consists of 128 code points.

As standard ASCII occupies 128 out of 256 possible code points, you can only make use of the remaining 128.

It's not enough for all possible languages, but it may be sufficient for one language, or for a small group of similar languages.

Can you set the higher half of the code points differently for different languages? Yes, you can. Such a concept is called a code page.

A code page is a standard for using the upper 128 code points to store specific national characters. For example, there are different code pages for Western Europe and Eastern Europe, Cyrillic and Greek alphabets, Arabic and Hebrew languages, and so on.

This means that the one and same code point can make different characters when used in different code pages.

For example, the code point 200 makes Č (a letter used by some Slavic languages) when utilized by the ISO/IEC 8859-2 code page, and makes Ш (a Cyrillic letter) when used by the ISO/IEC 8859-5 code page.
```