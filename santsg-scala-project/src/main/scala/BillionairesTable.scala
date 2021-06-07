import slick.jdbc.MySQLProfile.api._

class BillionairesTable(tag: Tag) extends  Table[(Option[Int], String, Double, String, String,
  Int, Int, String, String, String, Int, String, Boolean)](tag, "forbes-billionaires"){
  def id = column[Int]("id", O.PrimaryKey, O.AutoInc)
  def name = column[String]("Name")
  def net_worth = column[Double]("NetWorth")
  def country = column[String]("Country")
  def source = column[String]("Source")
  def rank = column[Int]("Rank")
  def age = column[Int]("Age")
  def residence = column[String]("Residence")
  def citizenship = column[String]("Citizenship")
  def status = column[String]("Status")
  def children = column[Int]("Children")
  def education = column[String]("Education")
  def self_made = column[Boolean]("Self_made")

  def * = (id.?,name,net_worth,country,source,rank,
    age,residence,citizenship,status,children,education,self_made)
}
