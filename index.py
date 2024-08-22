<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EAL Programming Language Documentation</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to EAL Programming Language</h1>
        <p>Your gateway to a powerful and intuitive programming experience.</p>
    </header>

    <nav>
        <ul>
            <li><a href="#introduction">Introduction</a></li>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#usage">Usage</a></li>
            <li><a href="#examples">Examples</a></li>
            <li><a href="#documentation">Documentation</a></li>
            <li><a href="#contributing">Contributing</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <main>
        <section id="introduction">
            <h2>Introduction</h2>
            <p>EAL (English Assembly Language) is a programming language designed to blend assembly-like efficiency with English-like readability and procedural, statically-typed syntax. It supports powerful features such as AOT reformatting, OTF compilation, JIT interpretation, and dynamic local virtual database (DLVD) integration.</p>
        </section>

        <section id="installation">
            <h2>Installation</h2>
            <p>To get started with EAL, follow these steps to install and set up the language environment.</p>
            <ol>
                <li>Clone the repository:
                    <pre><code>git clone https://github.com/JoeySoprano420/EAL-Programming-Language.git</code></pre>
                </li>
                <li>Navigate to the project directory:
                    <pre><code>cd EAL-Programming-Language</code></pre>
                </li>
                <li>Install required dependencies:
                    <pre><code>pip install -r requirements.txt</code></pre>
                </li>
                <li>Build the project:
                    <pre><code>python setup.py install</code></pre>
                </li>
            </ol>
        </section>

        <section id="usage">
            <h2>Usage</h2>
            <p>After installation, you can start using EAL by following these instructions:</p>
            <ol>
                <li>Create a new EAL file with a .eal extension.</li>
                <li>Write your EAL code in the file.</li>
                <li>Compile the code using the EAL compiler:
                    <pre><code>python eal/compiler.py --input your_code.eal --output your_code.bytecode</code></pre>
                </li>
                <li>Execute the compiled code using the EAL interpreter:
                    <pre><code>python eal/interpreter.py --input your_code.bytecode</code></pre>
                </li>
            </ol>
        </section>

        <section id="examples">
            <h2>Examples</h2>
            <p>Here are some example programs written in EAL:</p>
            <pre><code>
# Example EAL Program

>> Declaring variables
declare int x = 10;
declare bool flag = true;

>> Assembly-like operation
mov eax, 5
add eax, x

>> English-like command using Pentinary logic
if x is both greater than 5 and less than 15 then
    print "x is in range"
else if x is neither less than 5 nor greater than 15 then
    print "x is invalid"
else
    print "x is out of range"
            </code></pre>
        </section>

        <section id="documentation">
            <h2>Documentation</h2>
            <p>For detailed documentation, refer to the following files:</p>
            <ul>
                <li><a href="eal/programming_guide.pdf">EAL Programming Guide</a></li>
                <li><a href="eal/reference_manual.pdf">EAL Reference Manual</a></li>
            </ul>
        </section>

        <section id="contributing">
            <h2>Contributing</h2>
            <p>We welcome contributions to EAL! If you would like to contribute, please follow the guidelines in the <a href="CONTRIBUTING.md">CONTRIBUTING.md</a> file.</p>
        </section>

        <section id="contact">
            <h2>Contact</h2>
            <p>If you have any questions or need support, please reach out to us:</p>
            <ul>
                <li>Email: <a href="mailto:support@eal-lang.org">support@eal-lang.org</a></li>
                <li>GitHub Issues: <a href="https://github.com/JoeySoprano420/EAL-Programming-Language/issues">Submit an issue</a></li>
            </ul>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 EAL Programming Language. All rights reserved.</p>
    </footer>
</body>
</html>
