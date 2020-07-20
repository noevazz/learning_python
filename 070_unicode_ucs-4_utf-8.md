```
Unicode
    Code pages helped the computer industry to solve I18N issues for some time,
    but it soon turned out that they would not be a permanent solution.

    The concept that solved the problem in the long term was Unicode
    Unicode assigns unique (unambiguous) characters (letters, hyphens, ideograms, etc.)
    to more than a million code points. The first 128 Unicode code points are identical to ASCII,
    and the first 256 Unicode code points are identical to the ISO/IEC 8859-1 code page
    (a code page designed for western European languages).

UCS-4
    The Unicode standard says nothing about how to code and store the characters in the memory and files.
    It only names all available characters and assigns them to planes (a group of characters of similar origin, application, or nature).

    There is more than one standard describing the techniques used to implement Unicode in actual computers
    and computer storage systems. The most general of them is UCS-4
    
    The name comes from Universal Character Set.

    UCS-4 uses 32 bits (four bytes) to store each character, and the code is just the Unicode code points' unique number. A file containing UCS-4 encoded text may start with a BOM (byte order mark), an unprintable combination of bits announcing the nature of the file's contents. Some utilities may require it.

UTF-8
    As you can see, UCS-4 is a rather wasteful standard - it increases a text's size by four times compared to standard ASCII. Fortunately, there are smarter forms of encoding Unicode texts.

    The name is derived from Unicode Transformation Format.
    The concept is very smart. UTF-8 uses as many bits for each of the code points as it really needs to represent them.

    Due to features of the method used by UTF-8 to store the code points, there is no need to use the BOM, but some of the tools look for it when reading the file, and many editors set it up during the save.

    Python 3 fully supports Unicode and UTF-8:
        - you can use Unicode/UTF-8 encoded characters to name variables and other entities;
        - you can use them during all input and output.

This means that Python3 is completely I18Ned.
```