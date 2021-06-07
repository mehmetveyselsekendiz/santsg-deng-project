import akka.http.scaladsl.marshallers.sprayjson.SprayJsonSupport
import spray.json.DefaultJsonProtocol

object BillionaireJsonSupport extends DefaultJsonProtocol with SprayJsonSupport {
  implicit val PortofolioFormats = jsonFormat13(Billionaire)
}
