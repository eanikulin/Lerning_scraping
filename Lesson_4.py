import sqlite3

quotes_list = [{
                   'quote_text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.',
                   'quote_author': 'Albert Einstein', 'quotes_tags': ['change', 'deep-thoughts', 'thinking', 'world'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'It is our choices, Harry, that show what we truly are, far more than our abilities.',
                'quote_author': 'J.K. Rowling', 'quotes_tags': ['abilities', 'choices'],
                'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.',
                   'quote_author': 'Albert Einstein',
                   'quotes_tags': ['inspirational', 'life', 'live', 'miracle', 'miracles'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.',
                   'quote_author': 'Jane Austen', 'quotes_tags': ['aliteracy', 'books', 'classic', 'humor'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': "Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.",
                   'quote_author': 'Marilyn Monroe', 'quotes_tags': ['be-yourself', 'inspirational'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'Try not to become a man of success. Rather become a man of value.',
                'quote_author': 'Albert Einstein', 'quotes_tags': ['adulthood', 'success', 'value'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': 'It is better to be hated for what you are than to be loved for what you are not.',
                'quote_author': 'André Gide', 'quotes_tags': ['life', 'love'], 'source': 'quotes.toscrape.com'},
               {'quote_text': "I have not failed. I've just found 10,000 ways that won't work.",
                'quote_author': 'Thomas A. Edison',
                'quotes_tags': ['edison', 'failure', 'inspirational', 'paraphrased'], 'source': 'quotes.toscrape.com'},
               {'quote_text': "A woman is like a tea bag; you never know how strong it is until it's in hot water.",
                'quote_author': 'Eleanor Roosevelt', 'quotes_tags': ['misattributed-eleanor-roosevelt'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': 'A day without sunshine is like, you know, night.', 'quote_author': 'Steve Martin',
                'quotes_tags': ['humor', 'obvious', 'simile'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': "This life is what you make it. No matter what, you're going to mess up sometimes, it's a universal truth. But the good part is you get to decide how you're going to mess it up. Girls will be your friends - they'll act like it anyway. But just remember, some come, some go. The ones that stay with you through everything - they're your true best friends. Don't let go of them. Also remember, sisters make the best friends in the world. As for lovers, well, they'll come and go too. And baby, I hate to say it, most of them - actually pretty much all of them are going to break your heart, but you can't give up because if you give up, you'll never find your soulmate. You'll never find that half who makes you whole and that goes for everything. Just because you fail once, doesn't mean you're gonna fail at everything. Keep trying, hold on, and always, always, always believe in yourself, because if you don't, then who will, sweetie? So keep your head high, keep your chin up, and most importantly, keep smiling, because life's a beautiful thing and there's so much to smile about.",
                   'quote_author': 'Marilyn Monroe',
                   'quotes_tags': ['friends', 'heartbreak', 'inspirational', 'life', 'love', 'sisters'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.',
                   'quote_author': 'J.K. Rowling', 'quotes_tags': ['courage', 'friends'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': "If you can't explain it to a six year old, you don't understand it yourself.",
                'quote_author': 'Albert Einstein', 'quotes_tags': ['simplicity', 'understand'],
                'source': 'quotes.toscrape.com'}, {
                   'quote_text': "You may not be her first, her last, or her only. She loved before she may love again. But if she loves you now, what else matters? She's not perfect—you aren't either, and the two of you may never be perfect together but if she can make you laugh, cause you to think twice, and admit to being human and making mistakes, hold onto her and give her the most you can. She may not be thinking about you every second of the day, but she will give you a part of her that she knows you can break—her heart. So don't hurt her, don't change her, don't analyze and don't expect more than she can give. Smile when she makes you happy, let her know when she makes you mad, and miss her when she's not there.",
                   'quote_author': 'Bob Marley', 'quotes_tags': ['love'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living.',
                   'quote_author': 'Dr. Seuss', 'quotes_tags': ['fantasy'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'I may not have gone where I intended to go, but I think I have ended up where I needed to be.',
                   'quote_author': 'Douglas Adams', 'quotes_tags': ['life', 'navigation'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': "The opposite of love is not hate, it's indifference. The opposite of art is not ugliness, it's indifference. The opposite of faith is not heresy, it's indifference. And the opposite of life is not death, it's indifference.",
                   'quote_author': 'Elie Wiesel',
                   'quotes_tags': ['activism', 'apathy', 'hate', 'indifference', 'inspirational', 'love', 'opposite',
                                   'philosophy'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'It is not a lack of love, but a lack of friendship that makes unhappy marriages.',
                'quote_author': 'Friedrich Nietzsche',
                'quotes_tags': ['friendship', 'lack-of-friendship', 'lack-of-love', 'love', 'marriage',
                                'unhappy-marriage'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'Good friends, good books, and a sleepy conscience: this is the ideal life.',
                'quote_author': 'Mark Twain', 'quotes_tags': ['books', 'contentment', 'friends', 'friendship', 'life'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': 'Life is what happens to us while we are making other plans.',
                'quote_author': 'Allen Saunders',
                'quotes_tags': ['fate', 'life', 'misattributed-john-lennon', 'planning', 'plans'],
                'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'I love you without knowing how, or when, or from where. I love you simply, without problems or pride: I love you in this way because I do not know any other way of loving but this, in which there is no I or you, so intimate that your hand upon my chest is my hand, so intimate that when I fall asleep your eyes close.',
                   'quote_author': 'Pablo Neruda', 'quotes_tags': ['love', 'poetry'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'For every minute you are angry you lose sixty seconds of happiness.',
                'quote_author': 'Ralph Waldo Emerson', 'quotes_tags': ['happiness'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'If you judge people, you have no time to love them.', 'quote_author': 'Mother Teresa',
                'quotes_tags': ['attributed-no-source'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'Anyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.',
                   'quote_author': 'Garrison Keillor', 'quotes_tags': ['humor', 'religion'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'Beauty is in the eye of the beholder and it may be necessary from time to time to give a stupid or misinformed beholder a black eye.',
                   'quote_author': 'Jim Henson', 'quotes_tags': ['humor'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'Today you are You, that is truer than true. There is no one alive who is Youer than You.',
                   'quote_author': 'Dr. Seuss', 'quotes_tags': ['comedy', 'life', 'yourself'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'If you want your children to be intelligent, read them fairy tales. If you want them to be more intelligent, read them more fairy tales.',
                   'quote_author': 'Albert Einstein', 'quotes_tags': ['children', 'fairy-tales'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'It is impossible to live without failing at something, unless you live so cautiously that you might as well not have lived at all - in which case, you fail by default.',
                   'quote_author': 'J.K. Rowling', 'quotes_tags': [], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'Logic will get you from A to Z; imagination will get you everywhere.',
                'quote_author': 'Albert Einstein', 'quotes_tags': ['imagination'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'One good thing about music, when it hits you, you feel no pain.',
                'quote_author': 'Bob Marley', 'quotes_tags': ['music'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': "The more that you read, the more things you will know. The more that you learn, the more places you'll go.",
                   'quote_author': 'Dr. Seuss', 'quotes_tags': ['learning', 'reading', 'seuss'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'Of course it is happening inside your head, Harry, but why on earth should that mean that it is not real?',
                   'quote_author': 'J.K. Rowling', 'quotes_tags': ['dumbledore'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'The truth is, everyone is going to hurt you. You just got to find the ones worth suffering for.',
                   'quote_author': 'Bob Marley', 'quotes_tags': ['friendship'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'Not all of us can do great things. But we can do small things with great love.',
                'quote_author': 'Mother Teresa', 'quotes_tags': ['misattributed-to-mother-teresa', 'paraphrased'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': 'To the well-organized mind, death is but the next great adventure.',
                'quote_author': 'J.K. Rowling', 'quotes_tags': ['death', 'inspirational'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': "All you need is love. But a little chocolate now and then doesn't hurt.",
                'quote_author': 'Charles M. Schulz', 'quotes_tags': ['chocolate', 'food', 'humor'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': "We read to know we're not alone.", 'quote_author': 'William Nicholson',
                'quotes_tags': ['misattributed-to-c-s-lewis', 'reading'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'Any fool can know. The point is to understand.', 'quote_author': 'Albert Einstein',
                'quotes_tags': ['knowledge', 'learning', 'understanding', 'wisdom'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'I have always imagined that Paradise will be a kind of library.',
                'quote_author': 'Jorge Luis Borges', 'quotes_tags': ['books', 'library'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': 'It is never too late to be what you might have been.', 'quote_author': 'George Eliot',
                'quotes_tags': ['inspirational'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'A reader lives a thousand lives before he dies, said Jojen. The man who never reads lives only one.',
                   'quote_author': 'George R.R. Martin', 'quotes_tags': ['read', 'readers', 'reading', 'reading-books'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'You can never get a cup of tea large enough or a book long enough to suit me.',
                'quote_author': 'C.S. Lewis', 'quotes_tags': ['books', 'inspirational', 'reading', 'tea'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': 'You believe lies so you eventually learn to trust no one but yourself.',
                'quote_author': 'Marilyn Monroe', 'quotes_tags': [], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'If you can make a woman laugh, you can make her do anything.',
                'quote_author': 'Marilyn Monroe', 'quotes_tags': ['girls', 'love'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'Life is like riding a bicycle. To keep your balance, you must keep moving.',
                'quote_author': 'Albert Einstein', 'quotes_tags': ['life', 'simile'], 'source': 'quotes.toscrape.com'},
               {
                   'quote_text': 'The real lover is the man who can thrill you by kissing your forehead or smiling into your eyes or just staring into space.',
                   'quote_author': 'Marilyn Monroe', 'quotes_tags': ['love'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': "A wise girl kisses but doesn't love, listens but doesn't believe, and leaves before she is left.",
                   'quote_author': 'Marilyn Monroe', 'quotes_tags': ['attributed-no-source'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'Only in the darkness can you see the stars.', 'quote_author': 'Martin Luther King Jr.',
                'quotes_tags': ['hope', 'inspirational'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'It matters not what someone is born, but what they grow to be.',
                'quote_author': 'J.K. Rowling', 'quotes_tags': ['dumbledore'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'Love does not begin and end the way we seem to think it does. Love is a battle, love is a war; love is a growing up.',
                   'quote_author': 'James Baldwin', 'quotes_tags': ['love'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'There is nothing I would not do for those who are really my friends. I have no notion of loving people by halves, it is not my nature.',
                   'quote_author': 'Jane Austen', 'quotes_tags': ['friendship', 'love'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'Do one thing every day that scares you.', 'quote_author': 'Eleanor Roosevelt',
                'quotes_tags': ['attributed', 'fear', 'inspiration'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'I am good, but not an angel. I do sin, but I am not the devil. I am just a small girl in a big world trying to find someone to love.',
                   'quote_author': 'Marilyn Monroe', 'quotes_tags': ['attributed-no-source'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'If I were not a physicist, I would probably be a musician. I often think in music. I live my daydreams in music. I see my life in terms of music.',
                   'quote_author': 'Albert Einstein', 'quotes_tags': ['music'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'If you only read the books that everyone else is reading, you can only think what everyone else is thinking.',
                   'quote_author': 'Haruki Murakami', 'quotes_tags': ['books', 'thought'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'The difference between genius and stupidity is: genius has its limits.',
                'quote_author': 'Alexandre Dumas fils', 'quotes_tags': ['misattributed-to-einstein'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': "He's like a drug for you, Bella.", 'quote_author': 'Stephenie Meyer',
                'quotes_tags': ['drug', 'romance', 'simile'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'There is no friend as loyal as a book.', 'quote_author': 'Ernest Hemingway',
                'quotes_tags': ['books', 'friends', 'novelist-quotes'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'When one door of happiness closes, another opens; but often we look so long at the closed door that we do not see the one which has been opened for us.',
                   'quote_author': 'Helen Keller', 'quotes_tags': ['inspirational'], 'source': 'quotes.toscrape.com'},
               {'quote_text': "Life isn't about finding yourself. Life is about creating yourself.",
                'quote_author': 'George Bernard Shaw', 'quotes_tags': ['inspirational', 'life', 'yourself'],
                'source': 'quotes.toscrape.com'}, {
                   'quote_text': "That's the problem with drinking, I thought, as I poured myself a drink. If something bad happens you drink in an attempt to forget; if something good happens you drink in order to celebrate; and if nothing happens you drink to make something happen.",
                   'quote_author': 'Charles Bukowski', 'quotes_tags': ['alcohol'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'You don’t forget the face of the person who was your last hope.',
                'quote_author': 'Suzanne Collins', 'quotes_tags': ['the-hunger-games'],
                'source': 'quotes.toscrape.com'},
               {'quote_text': "Remember, we're madly in love, so it's all right to kiss me anytime you feel like it.",
                'quote_author': 'Suzanne Collins', 'quotes_tags': ['humor'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'To love at all is to be vulnerable. Love anything and your heart will be wrung and possibly broken. If you want to make sure of keeping it intact you must give it to no one, not even an animal. Wrap it carefully round with hobbies and little luxuries; avoid all entanglements. Lock it up safe in the casket or coffin of your selfishness. But in that casket, safe, dark, motionless, airless, it will change. It will not be broken; it will become unbreakable, impenetrable, irredeemable. To love is to be vulnerable.',
                   'quote_author': 'C.S. Lewis', 'quotes_tags': ['love'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'Not all those who wander are lost.', 'quote_author': 'J.R.R. Tolkien',
                'quotes_tags': ['bilbo', 'journey', 'lost', 'quest', 'travel', 'wander'],
                'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'Do not pity the dead, Harry. Pity the living, and, above all those who live without love.',
                   'quote_author': 'J.K. Rowling', 'quotes_tags': ['live-death-love'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'There is nothing to writing. All you do is sit down at a typewriter and bleed.',
                'quote_author': 'Ernest Hemingway', 'quotes_tags': ['good', 'writing'],
                'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'Finish each day and be done with it. You have done what you could. Some blunders and absurdities no doubt crept in; forget them as soon as you can. Tomorrow is a new day. You shall begin it serenely and with too high a spirit to be encumbered with your old nonsense.',
                   'quote_author': 'Ralph Waldo Emerson', 'quotes_tags': ['life', 'regrets'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'I have never let my schooling interfere with my education.',
                'quote_author': 'Mark Twain', 'quotes_tags': ['education'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': "I have heard there are troubles of more than one kind. Some come from ahead and some come from behind. But I've bought a big bat. I'm all ready you see. Now my troubles are going to have troubles with me!",
                   'quote_author': 'Dr. Seuss', 'quotes_tags': ['troubles'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'If I had a flower for every time I thought of you...I could walk through my garden forever.',
                   'quote_author': 'Alfred Tennyson', 'quotes_tags': ['friendship', 'love'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'Some people never go crazy. What truly horrible lives they must lead.',
                'quote_author': 'Charles Bukowski', 'quotes_tags': ['humor'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'The trouble with having an open mind, of course, is that people will insist on coming along and trying to put things in it.',
                   'quote_author': 'Terry Pratchett', 'quotes_tags': ['humor', 'open-mind', 'thinking'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'Think left and think right and think low and think high. Oh, the thinks you can think up if only you try!',
                   'quote_author': 'Dr. Seuss', 'quotes_tags': ['humor', 'philosophy'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': "What really knocks me out is a book that, when you're all done reading it, you wish the author that wrote it was a terrific friend of yours and you could call him up on the phone whenever you felt like it. That doesn't happen much, though.",
                   'quote_author': 'J.D. Salinger',
                   'quotes_tags': ['authors', 'books', 'literature', 'reading', 'writing'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'The reason I talk to myself is because I’m the only one whose answers I accept.',
                'quote_author': 'George Carlin',
                'quotes_tags': ['humor', 'insanity', 'lies', 'lying', 'self-indulgence', 'truth'],
                'source': 'quotes.toscrape.com'}, {
                   'quote_text': "You may say I'm a dreamer, but I'm not the only one. I hope someday you'll join us. And the world will live as one.",
                   'quote_author': 'John Lennon',
                   'quotes_tags': ['beatles', 'connection', 'dreamers', 'dreaming', 'dreams', 'hope', 'inspirational',
                                   'peace'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'I am free of all prejudice. I hate everyone equally. ', 'quote_author': 'W.C. Fields',
                'quotes_tags': ['humor', 'sinister'], 'source': 'quotes.toscrape.com'},
               {'quote_text': "The question isn't who is going to let me; it's who is going to stop me.",
                'quote_author': 'Ayn Rand', 'quotes_tags': [], 'source': 'quotes.toscrape.com'},
               {'quote_text': "′Classic′ - a book which people praise and don't read.", 'quote_author': 'Mark Twain',
                'quotes_tags': ['books', 'classic', 'reading'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'Anyone who has never made a mistake has never tried anything new.',
                'quote_author': 'Albert Einstein', 'quotes_tags': ['mistakes'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': "A lady's imagination is very rapid; it jumps from admiration to love, from love to matrimony in a moment.",
                   'quote_author': 'Jane Austen', 'quotes_tags': ['humor', 'love', 'romantic', 'women'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'Remember, if the time should come when you have to make a choice between what is right and what is easy, remember what happened to a boy who was good, and kind, and brave, because he strayed across the path of Lord Voldemort. Remember Cedric Diggory.',
                   'quote_author': 'J.K. Rowling', 'quotes_tags': ['integrity'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'I declare after all there is no enjoyment like reading! How much sooner one tires of any thing than of a book! -- When I have a house of my own, I shall be miserable if I have not an excellent library.',
                   'quote_author': 'Jane Austen', 'quotes_tags': ['books', 'library', 'reading'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'There are few people whom I really love, and still fewer of whom I think well. The more I see of the world, the more am I dissatisfied with it; and every day confirms my belief of the inconsistency of all human characters, and of the little dependence that can be placed on the appearance of merit or sense.',
                   'quote_author': 'Jane Austen', 'quotes_tags': ['elizabeth-bennet', 'jane-austen'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'Some day you will be old enough to start reading fairy tales again.',
                'quote_author': 'C.S. Lewis', 'quotes_tags': ['age', 'fairytales', 'growing-up'],
                'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'We are not necessarily doubting that God will do the best for us; we are wondering how painful the best will turn out to be.',
                   'quote_author': 'C.S. Lewis', 'quotes_tags': ['god'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time.',
                   'quote_author': 'Mark Twain', 'quotes_tags': ['death', 'life'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'A lie can travel half way around the world while the truth is putting on its shoes.',
                'quote_author': 'Mark Twain', 'quotes_tags': ['misattributed-mark-twain', 'truth'],
                'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'I believe in Christianity as I believe that the sun has risen: not only because I see it, but because by it I see everything else.',
                   'quote_author': 'C.S. Lewis', 'quotes_tags': ['christianity', 'faith', 'religion', 'sun'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'The truth." Dumbledore sighed. "It is a beautiful and terrible thing, and should therefore be treated with great caution.',
                   'quote_author': 'J.K. Rowling', 'quotes_tags': ['truth'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': "I'm the one that's got to die when it's time for me to die, so let me live my life the way I want to.",
                   'quote_author': 'Jimi Hendrix', 'quotes_tags': ['death', 'life'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'To die will be an awfully big adventure.', 'quote_author': 'J.M. Barrie',
                'quotes_tags': ['adventure', 'love'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'It takes courage to grow up and become who you really are.',
                'quote_author': 'E.E. Cummings', 'quotes_tags': ['courage'], 'source': 'quotes.toscrape.com'},
               {'quote_text': 'But better to get hurt by the truth than comforted with a lie.',
                'quote_author': 'Khaled Hosseini', 'quotes_tags': ['life'], 'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'You never really understand a person until you consider things from his point of view... Until you climb inside of his skin and walk around in it.',
                   'quote_author': 'Harper Lee', 'quotes_tags': ['better-life-empathy'],
                   'source': 'quotes.toscrape.com'}, {
                   'quote_text': 'You have to write the book that wants to be written. And if the book will be too difficult for grown-ups, then you write it for children.',
                   'quote_author': "Madeleine L'Engle",
                   'quotes_tags': ['books', 'children', 'difficult', 'grown-ups', 'write', 'writers', 'writing'],
                   'source': 'quotes.toscrape.com'},
               {'quote_text': 'Never tell the truth to people who are not worthy of it.', 'quote_author': 'Mark Twain',
                'quotes_tags': ['truth'], 'source': 'quotes.toscrape.com'},
               {'quote_text': "A person's a person, no matter how small.", 'quote_author': 'Dr. Seuss',
                'quotes_tags': ['inspirational'], 'source': 'quotes.toscrape.com'},
               {'quote_text': '... a mind needs books as a sword needs a whetstone, if it is to keep its edge.',
                'quote_author': 'George R.R. Martin', 'quotes_tags': ['books', 'mind'],
                'source': 'quotes.toscrape.com'}]

for tags in quotes_list:
    tags['quotes_tags'] = ', '.join(tags['quotes_tags'])

connection = sqlite3.connect('sqlite.db')

cursor = connection.cursor()

query = '''
    CREATE TABLE quotes(
        text TEXT,
        author TEXT,
        tags TEXT,
        sources TEXT
    )
'''
cursor.execute(query)
connection.commit()

insert_query = '''
    INSERT INTO quotes(
        text,
        author,
        tags,
        sources
    )
    VALUES(
        ?,
        ?,
        ?,
        ?
    )
'''

for quotes in quotes_list:
    quotes_tuple = tuple([v for v in dict.values(quotes)])
    cursor.execute(insert_query, quotes_tuple)
    connection.commit()
print(quotes_list)
