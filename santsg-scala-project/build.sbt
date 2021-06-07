name := "scala-v2"

version := "0.1"

scalaVersion := "2.13.6"

val akkaHttpVersion = "10.2.4"
val akkaVersion = "2.6.14"


libraryDependencies ++= Seq(
  "com.typesafe.akka" %% "akka-http" % akkaHttpVersion,
  "com.typesafe.akka" %% "akka-slf4j" % akkaVersion,
  // "ch.qos.logback" % "logback-classic" % "1.0.0" % "runtime",
  "com.typesafe.akka" %% "akka-http-spray-json" % akkaHttpVersion,
  "com.typesafe.akka" %% "akka-http-xml" % akkaHttpVersion,
  "com.typesafe.akka" %% "akka-stream" % akkaVersion,
  "com.typesafe.akka" %% "akka-http-testkit" % akkaHttpVersion % Test,
  "com.typesafe.akka" %% "akka-testkit" % akkaVersion % Test,
  "com.typesafe.akka" %% "akka-stream-testkit" % akkaVersion % Test,
  // "org.scalatest" %% "scalatest" % "3.0.1" % Test
  "com.typesafe.slick" %% "slick" % "3.3.3",
  "com.typesafe.slick" %% "slick-hikaricp" % "3.3.3",
  "com.typesafe.slick" %% "slick-codegen" % "3.3.3",
  "mysql" % "mysql-connector-java" % "5.1.24"
)

/*
// https://mvnrepository.com/artifact/com.typesafe.slick/slick
libraryDependencies += "com.typesafe.slick" %% "slick" % "3.3.3"

// https://mvnrepository.com/artifact/com.typesafe.slick/slick-hikaricp
libraryDependencies += "com.typesafe.slick" %% "slick-hikaricp" % "3.3.3"

// https://mvnrepository.com/artifact/com.typesafe.slick/slick-codegen
libraryDependencies += "com.typesafe.slick" %% "slick-codegen" % "3.3.3"

libraryDependencies += "mysql" % "mysql-connector-java" % "5.1.24"

 */


/*
// https://mvnrepository.com/artifact/com.typesafe.akka/akka-http
libraryDependencies += "com.typesafe.akka" %% "akka-http" % "10.2.4"

// https://mvnrepository.com/artifact/com.typesafe.akka/akka-actor
libraryDependencies += "com.typesafe.akka" %% "akka-actor" % "2.6.14"

// https://mvnrepository.com/artifact/com.typesafe.akka/akka-slf4j
libraryDependencies += "com.typesafe.akka" %% "akka-slf4j" % "2.6.14"

// https://mvnrepository.com/artifact/com.typesafe.akka/akka-http-spray-json
libraryDependencies += "com.typesafe.akka" %% "akka-http-spray-json" % "10.2.4"

 */


