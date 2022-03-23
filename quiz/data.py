# Questions from the https://opentdb.com/ API

question_data = [
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "The Harvard architecture for micro-controllers added which additional bus?",
     "correct_answer": "Instruction",
     "incorrect_answers": ["Address", "Data", "Control"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The HTML5 standard was published in 2014.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "What does CPU stand for?",
     "correct_answer": "Central Processing Unit",
     "incorrect_answers": ["Central Process Unit", "Computer Personal Unit",
                           "Central Processor Unit"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "Which internet company began life as an online bookstore called &#039;Cadabra&#039;?",
     "correct_answer": "Amazon",
     "incorrect_answers": ["eBay", "Overstock", "Shopify"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The first computer bug was formed by faulty wires.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "According to the International System of Units, how many bytes are in a kilobyte of RAM?",
     "correct_answer": "1000", "incorrect_answers": ["512", "1024", "500"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "FLAC stands for &quot;Free Lossless Audio Condenser&quot;&#039;",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "What was the name of the security vulnerability found in Bash in 2014?",
     "correct_answer": "Shellshock",
     "incorrect_answers": ["Heartbleed", "Bashbug", "Stagefright"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "Moore&#039;s law originally stated that the number of transistors on a microprocessor chip would double every...",
     "correct_answer": "Year",
     "incorrect_answers": ["Four Years", "Two Years", "Eight Years"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What does AD stand for in relation to Windows Operating Systems? ",
     "correct_answer": "Active Directory",
     "incorrect_answers": ["Alternative Drive", "Automated Database",
                           "Active Department"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What five letter word is the motto of the IBM Computer company?",
     "correct_answer": "Think", "incorrect_answers": ["Click", "Logic", "Pixel"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "Which of the following languages is used as a scripting language in the Unity 3D game engine?",
     "correct_answer": "C#", "incorrect_answers": ["Java", "C++", "Objective-C"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Pointers were not used in the original C programming language; they were added later on in C++.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "The series of the Intel HD graphics generation succeeding that of the 5000 and 6000 series (Broadwell) is called:",
     "correct_answer": "HD Graphics 500",
     "incorrect_answers": ["HD Graphics 700 ", "HD Graphics 600", "HD Graphics 7000"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What did the name of the Tor Anonymity Network orignially stand for?",
     "correct_answer": "The Onion Router",
     "incorrect_answers": ["The Only Router", "The Orange Router",
                           "The Ominous Router"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What was the first commerically available computer processor?",
     "correct_answer": "Intel 4004",
     "incorrect_answers": ["Intel 486SX", "TMS 1000", "AMD AM386"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "In web design, what does CSS stand for?",
     "correct_answer": "Cascading Style Sheet",
     "incorrect_answers": ["Counter Strike: Source", "Corrective Style Sheet",
                           "Computer Style Sheet"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "What is the domain name for the country Tuvalu?",
     "correct_answer": ".tv", "incorrect_answers": [".tu", ".tt", ".tl"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "RAM stands for Random Access Memory.", "correct_answer": "True",
     "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "The internet domain .fm is the country-code top-level domain for which Pacific Ocean island nation?",
     "correct_answer": "Micronesia",
     "incorrect_answers": ["Fiji", "Tuvalu", "Marshall Islands"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "How many kilobytes in one gigabyte (in decimal)?",
     "correct_answer": "1000000", "incorrect_answers": ["1024", "1000", "1048576"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "Generally, which component of a computer draws the most power?",
     "correct_answer": "Video Card",
     "incorrect_answers": ["Hard Drive", "Processor", "Power Supply"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "Which of these names was an actual codename for a cancelled Microsoft project?",
     "correct_answer": "Neptune",
     "incorrect_answers": ["Enceladus", "Pollux", "Saturn"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What is the name of the default theme that is installed with Windows XP?",
     "correct_answer": "Luna", "incorrect_answers": ["Neptune", "Whistler", "Bliss"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What is the correct term for the metal object in between the CPU and the CPU fan within a computer system?",
     "correct_answer": "Heat Sink",
     "incorrect_answers": ["CPU Vent", "Temperature Decipator", "Heat Vent"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "Which computer language would you associate Django framework with?",
     "correct_answer": "Python", "incorrect_answers": ["C#", "C++", "Java"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows 7 operating system has six main editions.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Windows ME operating system was released in the year 2000.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What does &quot;LCD&quot; stand for?",
     "correct_answer": "Liquid Crystal Display",
     "incorrect_answers": ["Language Control Design", "Last Common Difference",
                           "Long Continuous Design"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "The first dual-core CPU was the Intel Pentium D.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": ".at is the top-level domain for what country?",
     "correct_answer": "Austria",
     "incorrect_answers": ["Argentina", "Australia", "Angola"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "medium",
     "question": "It&#039;s not possible to format a write-protected DVD-R Hard Disk.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "What internet protocol was documented in RFC 1459?",
     "correct_answer": "IRC", "incorrect_answers": ["HTTP", "HTTPS", "FTP"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "Linux was first created as an alternative to Windows XP.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "Which of these is not a key value of Agile software development?",
     "correct_answer": "Comprehensive documentation",
     "incorrect_answers": ["Individuals and interactions", "Customer collaboration",
                           "Responding to change"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "This mobile OS held the largest market share in 2012.",
     "correct_answer": "iOS",
     "incorrect_answers": ["Android", "BlackBerry", "Symbian"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What was the first Android version specifically optimized for tablets?",
     "correct_answer": "Honeycomb",
     "incorrect_answers": ["Eclair", "Froyo", "Marshmellow"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "Laserjet and inkjet printers are both examples of what type of printer?",
     "correct_answer": "Non-impact printer",
     "incorrect_answers": ["Impact printer", "Daisywheel printer",
                           "Dot matrix printer"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "The C programming language was created by this American computer scientist. ",
     "correct_answer": "Dennis Ritchie",
     "incorrect_answers": ["Tim Berners Lee", "al-Khw\u0101rizm\u012b",
                           "Willis Ware"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "What vulnerability ranked #1 on the OWASP Top 10 in 2013?",
     "correct_answer": "Injection ",
     "incorrect_answers": ["Broken Authentication", "Cross-Site Scripting",
                           "Insecure Direct Object References"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "Approximately how many Apple I personal computers were created?",
     "correct_answer": "200", "incorrect_answers": ["100", "500", "1000"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "In programming, what do you call functions with the same name but different implementations?",
     "correct_answer": "Overloading",
     "incorrect_answers": ["Overriding", "Abstracting", "Inheriting"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "easy",
     "question": "In computing, what does LAN stand for?",
     "correct_answer": "Local Area Network",
     "incorrect_answers": ["Long Antenna Node", "Light Access Node",
                           "Land Address Navigation"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "Which of these is not a layer in the OSI model for data communications?",
     "correct_answer": "Connection Layer",
     "incorrect_answers": ["Application Layer", "Transport Layer", "Physical Layer"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "What type of sound chip does the Super Nintendo Entertainment System (SNES) have?",
     "correct_answer": "ADPCM Sampler",
     "incorrect_answers": ["FM Synthesizer", "Programmable Sound Generator (PSG)",
                           "PCM Sampler"]},
    {"category": "Science: Computers", "type": "boolean", "difficulty": "easy",
     "question": "The Python programming language gets its name from the British comedy group &quot;Monty Python.&quot;",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "medium",
     "question": "What does the &#039;S&#039; in the RSA encryption algorithm stand for?",
     "correct_answer": "Shamir",
     "incorrect_answers": ["Secure", "Schottky", "Stable"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "Which of the following computer components can be built using only NAND gates?",
     "correct_answer": "ALU", "incorrect_answers": ["CPU", "RAM", "Register"]},
    {"category": "Science: Computers", "type": "multiple", "difficulty": "hard",
     "question": "What is the codename of the eighth generation Intel Core micro-architecture launched in October 2017?",
     "correct_answer": "Coffee Lake",
     "incorrect_answers": ["Sandy Bridge", "Skylake", "Broadwell"]}
]
