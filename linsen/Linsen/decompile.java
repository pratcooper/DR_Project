import java.io.Reader;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.TreeSet;
import java.io.IOException;
import java.util.Iterator;
import java.util.Set;
import splitting.CompositeSplit;
import java.io.OutputStream;
import java.io.PrintStream;
import java.io.FileOutputStream;
import splitting.SplitTokenModuleFactory;
import java.util.List;
import indexing.index.IndexFactory;
import indexing.index.IndexLucene;
import java.util.LinkedList;
import java.util.ResourceBundle;

// 
// Decompiled by Procyon v0.5.30
// 

public class NormalizeMain
{
    public static void main(final String[] args) throws IOException, RuntimeException {
        final String outputTestSet = ResourceBundle.getBundle("ConfigurationTestSet").getString("output_test_set");
        final String pathAcronymsFile = ResourceBundle.getBundle("ConfigurationTestSet").getString("acronyms_file");
        final String rootProject = ResourceBundle.getBundle("ConfigurationTestSet").getString("root_project");
        final String pathStopWordsTestSet = ResourceBundle.getBundle("ConfigurationTestSet").getString("path_stopwords_test_set");
        final String pathAbbreviationsFile = ResourceBundle.getBundle("ConfigurationTestSet").getString("abbreviations_file");
        final String rootReportFolderPath = ResourceBundle.getBundle("ConfigurationTestSet").getString("root_report");
        final String extensionIndexingFile = ResourceBundle.getBundle("ConfigurationTestSet").getString("extension_indexing_file");
        final String targetFilePathToAnalyse = ResourceBundle.getBundle("ConfigurationTestSet").getString("target_file_path");
        final String targetIdentifersFilePath = ResourceBundle.getBundle("ConfigurationTestSet").getString("target_identifiers_list");
        final LinkedList<String> externalDictionaries = new LinkedList<String>();
        final IndexLucene targetSystemData = (IndexLucene)IndexFactory.createIndex(outputTestSet, externalDictionaries, rootProject, pathStopWordsTestSet, pathAcronymsFile, pathAbbreviationsFile, extensionIndexingFile, IndexFactory.ALL);
        final CompositeSplit splitter = SplitTokenModuleFactory.createPatternMatchingSplittingModule();
        final List<String> allFile = targetSystemData.getAllIndexedFiles();
        if (!allFile.contains(targetFilePathToAnalyse)) {
            System.exit(-1);
        }
        final String targetFileName = targetFilePathToAnalyse.substring(targetFilePathToAnalyse.lastIndexOf(47) + 1, targetFilePathToAnalyse.lastIndexOf(46));
        final FileOutputStream reportFile = new FileOutputStream(rootReportFolderPath + targetFileName + ".txt");
        final PrintStream outputReportFile = new PrintStream(reportFile);
        final Set<String> allIdentifiers = targetSystemData.getTokenDocument(targetFilePathToAnalyse);
        final Set<String> targetIdentifiers = loadTargetIdentifiersList(targetIdentifersFilePath);
        for (final String identifier : allIdentifiers) {
            if (targetIdentifiers.contains(identifier.toLowerCase())) {
                splitter.split(identifier, 1, targetFilePathToAnalyse);
                final List<String> transformationMap = splitter.getTrasformationMap(identifier);
                outputReportFile.print(identifier + ":=");
                for (final String token : transformationMap) {
                    outputReportFile.print(token + ",");
                }
                outputReportFile.println();
            }
        }
        outputReportFile.close();
    }
    
    private static Set<String> loadTargetIdentifiersList(final String targetIdentifiersListFilePath) {
        final Set<String> targetIdentifiersList = new TreeSet<String>();
        try {
            final BufferedReader bufferReader = new BufferedReader(new FileReader(targetIdentifiersListFilePath));
            String line = "";
            do {
                try {
                    line = bufferReader.readLine();
                    if (line != null) {
                        targetIdentifiersList.add(line.trim().toLowerCase());
                    }
                }
                catch (IOException ioExceptionBufferedReader) {
                    break;
                }
            } while (line != null && line.length() >= 0);
        }
        catch (IOException ex) {}
        return targetIdentifiersList;
    }
}
