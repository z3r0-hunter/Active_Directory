1-First task as domain administrator is to check the existing AD OUs and users

2-Deleting extra OUs and users 
   if you click and delete the ou -> this return error  as by defualt OUs protected against accidental deletion

   to delete it view > Advanced Features > object > click on [] protect object from accidental deletion

3-Delegation
  process that give users some control over some OUs
  .allow to grant user to perform advanced tasks on OUs without needing a Domain administrator to step in

  steps
  choose OUs and right click > delegate Control > add > Enter the object names > check names