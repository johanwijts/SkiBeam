using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WPFopdracht
{
    public class Customer
    {
        public string name;
        public int id;

        public List<int> ordersById = new List<int>();

        public Customer(string inputName, int countId)
        {
            name = inputName;
            id = countId;            
        }
        
        public void addOrderToCustomer(int orderId)
        {
            this.ordersById.Add(orderId);
        }
    }

    public class Product
    {
        public string name;
        public int id;
        public string productGroup;

        public Product(string inputName, int countId, string selectGroup)
        {
            name = inputName;
            id = countId;
            productGroup = selectGroup;
        }
    }

    public class Order
    {
        public int id;
        public DateTime date;

        public string customer;

        public List<string> products = new List<string>();

        public Order(int countId)
        {
            id = countId;
        }

        public void addProducts(string inputOrder)
        {
            this.products.Add(inputOrder);
        }

        public void addDate(DateTime selectedDate)
        {
            this.date = selectedDate;
        }
    }

    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        //Instead of using a Database we'll keep our information stored here
        List<Customer> customers = new List<Customer>();
        List<Product> products = new List<Product>();
        List<string> productGroups = new List<string>();
        List<Order> orders = new List<Order>();
        List<string> productsInOrder = new List<string>();

        private void addCustomerButton_Click(object sender, RoutedEventArgs e)
        {
            string resultCustomer = nameTextBox.Text.ToString();

            if (resultCustomer == "")
            {
                errorAddCustomer.Content = "Please enter a name";
                return;
            }

            else
            {
                errorAddCustomer.Content = "";

                foreach (var customerItem in customers)
                {
                    if (customerItem.name == nameTextBox.Text.ToString())
                    {
                        errorAddCustomer.Content = "Customer already exists";
                        return;
                    }                       
                }

                int customerNumber = customers.Count;
                Customer customer = new Customer(resultCustomer, customerNumber);
                customers.Add(customer);

                //Product was successfully added, reset the content
                nameTextBox.Text = "";
                errorAddCustomer.Content = "";
            }
        }

        private void addProductButton_Click(object sender, RoutedEventArgs e)
        {
            string resultProduct = productTextBox.Text.ToString();
            string productGroup = selectGroupComboBox.Text.ToString();

            if (resultProduct == "" || resultProduct.Any(char.IsDigit))
            {
                productTextBox.Text = "";
                wrongProductLabel.Content = "Please enter a valid product";
                return;
            }

            else if (productGroup == "")
            {
                forgotGroupSelectionLabel.Content = "Did you forget the group?";
                wrongProductLabel.Content = "";
                return;
            }

            else
            {
                wrongProductLabel.Content = "";

                foreach (var productItem in products)
                {
                    if (productTextBox.Text == productItem.name)
                    {
                        wrongProductLabel.Content = "Product already exists";
                        return;
                    }
                }

                int productNumber = products.Count;

                Product product = new Product(resultProduct, productNumber, productGroup);

                products.Add(product);
                productGroups.Add(productGroup);

                //Product was successfully added, reset the content
                productTextBox.Text = "";
                forgotGroupSelectionLabel.Content = "";
                wrongProductLabel.Content = "";
            }
        }

        private void selectedProductToAddComboBox_DropDownOpened(object sender, EventArgs e)
        {
            selectedProductToAddComboBox.Items.Clear();

            foreach (var product in products)
            {
                if (getProductGroupComboBox.Text == product.productGroup)
                {
                    selectedProductToAddComboBox.Items.Add(product.name);
                }
            }
        }

        private void selectCustomerComboBox_DropDownOpened(object sender, EventArgs e)
        {
            selectCustomerComboBox.Items.Clear();

            foreach (var customer in customers)
            {                
                 selectCustomerComboBox.Items.Add(customer.name);                
            }
        }

        private void addProductToOrderButton_Click(object sender, RoutedEventArgs e)
        {
            if (!(selectedProductToAddComboBox.Text == ""))
            {
                string finalProduct;
                finalProduct = selectedProductToAddComboBox.Text.ToString();
                finalProduct = finalProduct + " x " + multiplyerTextBox.Text.ToString();
                productsInOrder.Add(finalProduct);

                selectedProductToAddComboBox.Text = "";
                multiplyerTextBox.Text = "1";
            }

            else
            {
                //notify user to select a product and group
            }
        }

        private void finishOrderButton_Click(object sender, RoutedEventArgs e)
        {
            //Validation check for Customer and prevent a empty Order
            if (!(selectCustomerComboBox.Text == "") & productsInOrder.Count > 0 & !(selectOrderDate.SelectedDate == null))
            {
                Order order = new Order(orders.Count);
                
                //Add all the products to the Order object
                foreach (var product in productsInOrder)
                {
                    order.addProducts(product);                                   
                }

                //Set the date for the order
                order.addDate((DateTime)selectOrderDate.SelectedDate);

                //Look for the selected Customer and add the Order id
                foreach (var customer in customers)
                {
                    if (customer.name == selectCustomerComboBox.Text.ToString())
                    {
                        customer.addOrderToCustomer(order.id);
                    }
                }

                //Save the order
                orders.Add(order);

                //Notify user that the order was succesful
                finishOrderResultLabel.Content = "Order for " + selectCustomerComboBox.Text + " succesful";

                //Clear the order list and input for next use
                productsInOrder.Clear();
                getProductGroupComboBox.Text = "";
                selectedProductToAddComboBox.Text = "";
                selectCustomerComboBox.Text = "";               
            }

            else
            {
                //add a notifier that something is missing
                finishOrderResultLabel.Content = "Did you forget something?";
            }
        }

        private void selectSearchButton_Click(object sender, RoutedEventArgs e)
        {
            //Starting the search we clear possible old Values
            searchNotFoundLabel.Content = "";
            searchSelectorComboBox.Items.Clear();

            if (!(selectSearchTypeComboBox.Text == "") & !(searchForOrderTextBox.Text == ""))
            {
                if (selectSearchTypeComboBox.Text == "Customer")
                {
                    foreach (var customer in customers)
                    {
                        if (customer.name == searchForOrderTextBox.Text)
                        {
                            foreach (var orderId in customer.ordersById)
                            {
                                string searchSelectorItem = "Order " + orderId.ToString();
                                searchSelectorComboBox.Items.Add(searchSelectorItem);
                            }

                            searchNotFoundLabel.Content = "Customer " + customer.name + " Found";
                            return;
                        }
                    }

                    searchNotFoundLabel.Content = "Customer not Found";
                }
         
                else if (selectSearchTypeComboBox.Text == "Product")
                {
                    foreach (var product in products)
                    {
                        if (product.name == searchForOrderTextBox.Text)
                        {
                            //Because our products in a order contain an amount, we're gonna search for them using a letter count
                            int letterCount = searchForOrderTextBox.Text.Length;

                            //Go through each order in orders
                            foreach (var order in orders)
                            {
                                //Go through each product in order
                                foreach (var item in order.products)
                                {
                                    //We found our item and add the whole order to the combobox
                                    if (item.Substring(0, letterCount) == searchForOrderTextBox.Text)
                                    {
                                        string searchSelectorItem = "Order " + order.id.ToString();
                                        searchSelectorComboBox.Items.Add(searchSelectorItem);
                                    }
                                }
                            }

                            searchNotFoundLabel.Content = "Product " + product.name + " Found";
                            return;
                        }
                    }

                    searchNotFoundLabel.Content = "Product not Found";
                }

                else 
                { 
                    //Nothing for now, unless we add more selections
                }
            }

            else
            {
                //add a notifier that something is missing
            }
        }

        private void searchSelectorComboBox_DropDownClosed(object sender, EventArgs e)
        {
            //Reset the list for new use
            resultSearchListBox.Items.Clear();

            if (selectSearchTypeComboBox.Text == "Customer" & !(searchSelectorComboBox.Text == ""))
            {
                int selectedCustomerId = Int32.Parse(searchSelectorComboBox.Text.Substring(6));
                
                foreach (var product in orders[selectedCustomerId].products)
                {
                    resultSearchListBox.Items.Add(product);
                }
            }

            else if (selectSearchTypeComboBox.Text == "Product" & !(searchSelectorComboBox.Text == ""))
            {
                int selectedProductId = Int32.Parse(searchSelectorComboBox.Text.Substring(6));

                foreach (var product in orders[selectedProductId].products)
                {
                    resultSearchListBox.Items.Add(product);
                }
            }

            else
            {
                //Check if theres a date
                if (!(selectSearchDate == null) & !(searchSelectorComboBox.Text == ""))
                {
                    int selectedProductId = Int32.Parse(searchSelectorComboBox.Text.Substring(6));

                    foreach (var product in orders[selectedProductId].products)
                    {
                        resultSearchListBox.Items.Add(product);
                    }
                }

                //We checked every parameter there is, do nothing really
            }
        }

        private void searchWithDate_CalendarClosed(object sender, RoutedEventArgs e)
        {
            //Starting the search we clear possible old Values
            searchNotFoundLabel.Content = "";
            searchSelectorComboBox.Items.Clear();

            foreach (var order in orders)
            {
                if (order.date == searchWithDate.SelectedDate)
                {
                    string searchSelectorItem = "Order " + order.id.ToString();
                    searchSelectorComboBox.Items.Add(searchSelectorItem);
                }
            }
        }
    }
}
