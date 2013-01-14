Feature: Rocking with lettuce and django

    Scenario: Simple Hello World
        Given I access the url "/"
        Then I see the header "Hello World"

    Scenario: Hello + capitalized name
        Given I access the url "/some-name"
        Then I see the header "Hello Some Name"