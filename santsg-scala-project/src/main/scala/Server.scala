import akka.actor.ActorSystem
import akka.http.scaladsl.Http
import akka.http.scaladsl.server.Directives._
import akka.stream.ActorMaterializer

import scala.concurrent.Await
import scala.concurrent.duration.Duration
import BillionaireJsonSupport._


object Server extends App {

  implicit val actorSystem = ActorSystem("AkkaHTTPServices")
  implicit val materializer = ActorMaterializer()

  val apiRoutes =
    post {
      entity(as[Billionaire]) { billionaire =>
        complete(s"Name: ${billionaire.Name} => NetWorth: ${billionaire.NetWorth}")
      }
    }

  Http().bindAndHandle(apiRoutes, "localhost", 8080)
  Await.result(actorSystem.whenTerminated, Duration.Inf)

}

// Post API
// https://doc.akka.io/docs/akka-http/current/routing-dsl/directives/marshalling-directives/entity.html

