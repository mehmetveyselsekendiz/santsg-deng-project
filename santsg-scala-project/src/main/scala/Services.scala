import slick.jdbc.JdbcBackend.Database
import slick.lifted.TableQuery

class Services{

  val db = Database.forConfig("database")

  val billionaires = TableQuery[BillionairesTable]


}
