
#Feature: User can open the product detail and verify that the sale status is correct




  #Scenario:User can open the product and verify sale status

   #Given Open main page
    #When Login to the page using "salahmechou10@outlook.com" and "Salah1992."
    #And Click on "off plan" in the left side menu
    #Then Verify "off plan" page is opened
    #Then check the status of the first product
    #And click the first product
    #Then Verify the sale status is correct


   Feature: Verify Product Sale Status
  As a user
  I want to open product details
  So that I can verify the sale status is correct

  Scenario: User can open the product detail and verify that the sale status is correct
    Given I am on the main page "https://soft.reelly.io/sign-in"
    When I log in to the page
    And I click on "off plan" in the left side menu
    And I check the sale status of the first product
    And I click the first product
    Then I verify that in the Details section, the sale status is correct