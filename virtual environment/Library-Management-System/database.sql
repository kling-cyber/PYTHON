BEGIN TRANSACTION;
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL,
    availability_status TEXT NOT NULL
);
INSERT INTO "books" VALUES(1,'The Great Gatsby','F. Scott Fitzgerald','Fiction','Available');
INSERT INTO "books" VALUES(2,'The Great Gatsby','F. Scott Fitzgerald','Fiction','Available');
INSERT INTO "books" VALUES(3,'The Great Gatsby','F. Scott Fitzgerald','Fiction','Available');
INSERT INTO "books" VALUES(4,'The Great Gatsby','F. Scott Fitzgerald','Fiction','Available');
INSERT INTO "books" VALUES(5,'The Great Gatsby','F. Scott Fitzgerald','Fiction','Available');
INSERT INTO "books" VALUES(6,'To Kill a Mockingbird','Harper Lee','Fiction','Available');
INSERT INTO "books" VALUES(7,'1984','George Orwell','Dystopian','Available');
INSERT INTO "books" VALUES(8,'Pride and Prejudice','Jane Austen','Romance','Available');
INSERT INTO "books" VALUES(9,'The Catcher in the Rye','J.D. Salinger','Fiction','Available');
INSERT INTO "books" VALUES(10,'The Hobbit','J.R.R. Tolkien','Fantasy','Available');
INSERT INTO "books" VALUES(11,'The Great Gatsby','F. Scott Fitzgerald','Fiction','Available');
INSERT INTO "books" VALUES(12,'To Kill a Mockingbird','Harper Lee','Fiction','Available');
INSERT INTO "books" VALUES(13,'1984','George Orwell','Dystopian','Available');
INSERT INTO "books" VALUES(14,'Pride and Prejudice','Jane Austen','Romance','Available');
INSERT INTO "books" VALUES(15,'The Catcher in the Rye','J.D. Salinger','Fiction','Available');
INSERT INTO "books" VALUES(16,'The Hobbit','J.R.R. Tolkien','Fantasy','Available');
INSERT INTO "books" VALUES(17,'The Great Gatsby','F. Scott Fitzgerald','Fiction','Available');
INSERT INTO "books" VALUES(18,'To Kill a Mockingbird','Harper Lee','Fiction','Available');
INSERT INTO "books" VALUES(19,'1984','George Orwell','Dystopian','Available');
INSERT INTO "books" VALUES(20,'Pride and Prejudice','Jane Austen','Romance','Available');
INSERT INTO "books" VALUES(21,'The Catcher in the Rye','J.D. Salinger','Fiction','Available');
INSERT INTO "books" VALUES(22,'The Hobbit','J.R.R. Tolkien','Fantasy','Available');
INSERT INTO "books" VALUES(23,'The Great Gatsby','F. Scott Fitzgerald','Fiction','Available');
INSERT INTO "books" VALUES(24,'To Kill a Mockingbird','Harper Lee','Fiction','Available');
INSERT INTO "books" VALUES(25,'1984','George Orwell','Dystopian','Available');
INSERT INTO "books" VALUES(26,'Pride and Prejudice','Jane Austen','Romance','Available');
INSERT INTO "books" VALUES(27,'The Catcher in the Rye','J.D. Salinger','Fiction','Available');
INSERT INTO "books" VALUES(28,'The Hobbit','J.R.R. Tolkien','Fantasy','Available');
COMMIT;
