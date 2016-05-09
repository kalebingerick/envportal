# [EnvPortal](https://safe-cliffs-39205.herokuapp.com/)

Created by John Sellers, Kaleb Davis, Scott Ketelaar, Arron Reed, and Daniel Fehrenbach

For __SWEN 444 UI Design Project__

EnvPortal is a web-based application designed to make it easy for any user to research environmental resources and events in their communities, as well as creating events for others to attend.

## System Installation

To visit this site, go to https://safe-cliffs-39205.herokuapp.com.

To add features and develop, follow these steps:

1. Clone the repository.
2. Create a virtualenv by running the command `mkvirtualenv {name}` (assuming virtualenvwrapper is installed)
3. Start work on the virtualenv by running `workon {name}`
4. Install the dependencies and packages by running `pip install -r requirements.txt`
5. Run the application `python manage.py runserver`

## Features:
	
### Make account -- Create an account to interact with other users, and to create and attend events!
- User will navigate to the “Sign Up” page.
- User will be provided with sample information for the forms.
- User will be redirected to the “Validation Email Sent” page.

### Find Resources -- Search around your location to find environmental resources near you!
- User will navigate to the “Find Resources” page.
- User will activate the search on the page.
- User sees a list of pre-populated resources.

### Sign Up For Event -- Explore user created events and choose which ones you would like to attend!
- User navigates to “Find Events” page.
- User selects a day on the calendar with an event.
- User clicks on “Attend Event”.
- User will be redirected to the “Attending Event” page.

### Create Event -- Make your own events for other members to attend!
- User navigates to “Create Event” page.
- User will be provided with sample information for the forms.
- User will be redirected to the “Event Created” page.

### Edit Event -- Update or fix information in your created events!
- User navigates to “My Events” page.
- User clicks on “Edit Event”.
- User changes forms and submits.
- User will be redirected to the “Event Updated” page.
	
## Unsupported Features/Bugs

Currently the site has no backend. All of the events and such are hardcoded into the site, since this is a beta version. This will be addressed as work on the site moves forward.
