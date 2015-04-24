//
//  EventDetailViewController.swift
//  EventApp
//
//  Created by Christopher weber on 24.04.15.
//  Copyright (c) 2015 BFH. All rights reserved.
//

import UIKit

class EventDetailViewController: UIViewController {

    @IBOutlet var eventNameLabel: UILabel!
    var eventName: String?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.eventNameLabel.text = self.eventName
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
